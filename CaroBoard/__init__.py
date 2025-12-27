from type import BlockMode, PositionType, SideReturnType


class CaroBoard:
    size: int
    current_player: int
    board: list[list[int]]

    def __init__(self, size=5):
        self.size = size
        self.current_player = 1
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def _check_direction_win(
        self, position: PositionType, vector: PositionType
    ) -> SideReturnType:
        counter = 0
        pointer = [position[0] + vector[0], position[1] + vector[1]]
        block_mode: BlockMode = None
        while (
            0 <= pointer[0] < self.size and 0 <= pointer[1] < self.size and counter <= 4
        ):
            _player = self.board[pointer[0]][pointer[1]]
            if _player == 0:
                break
            elif _player != self.current_player:
                block_mode = "opposite"
                break
            else:
                if (
                    0 > pointer[0]
                    or pointer[0] >= self.size
                    or 0 > pointer[1]
                    or pointer[1] >= self.size
                ):
                    block_mode = "wall"
                    break
            pointer = [pointer[0] + vector[0], pointer[1] + vector[1]]
            ++counter
        return {"counter": counter, "blockMode": block_mode}

    def _check_horizontal_win(self, position: PositionType):
        left_horizontal_win = self._check_direction_win(position, [0, -1])
        right_horizontal_win = self._check_direction_win(position, [0, 1])
        total_pieces = left_horizontal_win["counter"] + right_horizontal_win["counter"]
        is_block_two_side = (
            left_horizontal_win["blockMode"] == "opposite"
            and right_horizontal_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_vertical_win(self, position: PositionType):
        top_vertical_win = self._check_direction_win(position, [-1, 0])
        bottom_vertical_win = self._check_direction_win(position, [1, 0])
        total_pieces = top_vertical_win["counter"] + bottom_vertical_win["counter"]
        is_block_two_side = (
            top_vertical_win["blockMode"] == "opposite"
            and bottom_vertical_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_left_diagonal_win(self, position: PositionType):
        top_left_diagonal_win = self._check_direction_win(position, [-1, -1])
        bottom_left_diagonal_win = self._check_direction_win(position, [1, 1])
        total_pieces = (
            top_left_diagonal_win["counter"] + bottom_left_diagonal_win["counter"]
        )
        is_block_two_side = (
            top_left_diagonal_win["blockMode"] == "opposite"
            and bottom_left_diagonal_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_right_diagonal_win(self, position: PositionType):
        top_right_diagonal_win = self._check_direction_win(position, [-1, 1])
        bottom_right_diagonal_win = self._check_direction_win(position, [1, -1])
        total_pieces = (
            top_right_diagonal_win["counter"] + bottom_right_diagonal_win["counter"]
        )
        is_block_two_side = (
            top_right_diagonal_win["blockMode"] == "opposite"
            and bottom_right_diagonal_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_win(self, position: PositionType):
        counter = 0
        if self._check_horizontal_win(position):
            ++counter
        if self._check_vertical_win(position):
            ++counter
        if self._check_left_diagonal_win(position):
            ++counter
        if self._check_right_diagonal_win(position):
            ++counter
        return counter

    def _switch_current_player(self):
        self.current_player = 3 - self.current_player
        return self.current_player

    def move(self, position: PositionType):
        self.board[position[0]][position[1]] = self.current_player
        if self._check_win(position) > 0:
            return True
        self._switch_current_player()
        return False

    def draw(self):
        print("***************************")
        for row in range(self.size):
            for _ in range(2 * self.size):
                print(end="-")
            print()
            for column in range(self.size):
                print(self.board[row][column], end="|")
            print()
        print("***************************")

    def reset(self):
        self.current_player = 0
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
