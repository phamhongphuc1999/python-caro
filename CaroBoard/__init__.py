from type import (
    DOWN_LEFT,
    DOWN_RIGHT,
    DOWN_VERTICAL,
    EMPTY,
    LEFT_HORIZONTAL,
    PLAYER1,
    RIGHT_HORIZONTAL,
    UP_LEFT,
    UP_RIGHT,
    UP_VERTICAL,
    BlockMode,
    PositionType,
    SideReturnType,
)


class CaroBoard:
    size: int
    current_player: int
    board: list[list[int]]

    def __init__(self, size=5):
        self.size = size
        self.current_player = PLAYER1
        self.board = [[EMPTY for _ in range(size)] for _ in range(size)]

    def load_board(self, current_player: int, board: list[list[int]]):
        if len(board) != len(board[0]):
            raise SyntaxError("size is invalid")
        self.current_player = current_player
        self.board = board
        self.size = len(board)

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
            pointer = [pointer[0] + vector[0], pointer[1] + vector[1]]
            counter = counter + 1
        if (
            pointer[0] < 0
            or pointer[0] >= self.size
            or pointer[1] < 0
            or pointer[1] >= self.size
        ):
            block_mode = "wall"
        return {"counter": counter, "blockMode": block_mode}

    def _check_horizontal_win(self, position: PositionType):
        left_win = self._check_direction_win(position, LEFT_HORIZONTAL)
        right_win = self._check_direction_win(position, RIGHT_HORIZONTAL)
        total_pieces = left_win["counter"] + right_win["counter"]
        is_block_two_side = (
            left_win["blockMode"] == "opposite" and right_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_vertical_win(self, position: PositionType):
        up_win = self._check_direction_win(position, UP_VERTICAL)
        down_win = self._check_direction_win(position, DOWN_VERTICAL)
        total_pieces = up_win["counter"] + down_win["counter"]
        is_block_two_side = (
            up_win["blockMode"] == "opposite" and down_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_left_diagonal_win(self, position: PositionType):
        up_left_win = self._check_direction_win(position, UP_LEFT)
        down_right_win = self._check_direction_win(position, DOWN_RIGHT)
        total_pieces = up_left_win["counter"] + down_right_win["counter"]
        is_block_two_side = (
            up_left_win["blockMode"] == "opposite"
            and down_right_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_right_diagonal_win(self, position: PositionType):
        up_right_win = self._check_direction_win(position, UP_RIGHT)
        down_left_win = self._check_direction_win(position, DOWN_LEFT)
        total_pieces = up_right_win["counter"] + down_left_win["counter"]
        is_block_two_side = (
            up_right_win["blockMode"] == "opposite"
            and down_left_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    def _check_win(self, position: PositionType):
        counter = 0
        if self._check_horizontal_win(position):
            counter = counter + 1
        if self._check_vertical_win(position):
            counter = counter + 1
        if self._check_left_diagonal_win(position):
            counter = counter + 1
        if self._check_right_diagonal_win(position):
            counter = counter + 1
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
        self.current_player = PLAYER1
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
