from CaroBoard.utils import is_in_board
from type import (
    DOWN_LEFT,
    DOWN_RIGHT,
    DOWN_VERTICAL,
    LEFT_HORIZONTAL,
    RIGHT_HORIZONTAL,
    UP_LEFT,
    UP_RIGHT,
    UP_VERTICAL,
    BlockMode,
    PositionType,
    SideReturnType,
)


class CaroWin:
    @staticmethod
    def _check_direction_win(
        board: list[list[int]],
        size: int,
        current_player: int,
        position: PositionType,
        vector: PositionType,
    ) -> SideReturnType:
        counter = 0
        pointer = [position[0] + vector[0], position[1] + vector[1]]
        block_mode: BlockMode = None
        while 0 <= pointer[0] < size and 0 <= pointer[1] < size and counter <= 4:
            _player = board[pointer[0]][pointer[1]]
            if _player == 0:
                break
            elif _player != current_player:
                block_mode = "opposite"
                break
            pointer = [pointer[0] + vector[0], pointer[1] + vector[1]]
            counter = counter + 1
        if not is_in_board(pointer[0], pointer[1], size):
            block_mode = "wall"
        return {"counter": counter, "blockMode": block_mode}

    @staticmethod
    def _check_horizontal_win(
        board: list[list[int]], size: int, current_player: int, position: PositionType
    ):
        left_win = CaroWin._check_direction_win(
            board, size, current_player, position, LEFT_HORIZONTAL
        )
        right_win = CaroWin._check_direction_win(
            board, size, current_player, position, RIGHT_HORIZONTAL
        )
        total_pieces = left_win["counter"] + right_win["counter"]
        is_block_two_side = (
            left_win["blockMode"] == "opposite" and right_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    @staticmethod
    def _check_vertical_win(
        board: list[list[int]], size: int, current_player: int, position: PositionType
    ):
        up_win = CaroWin._check_direction_win(
            board, size, current_player, position, UP_VERTICAL
        )
        down_win = CaroWin._check_direction_win(
            board, size, current_player, position, DOWN_VERTICAL
        )
        total_pieces = up_win["counter"] + down_win["counter"]
        is_block_two_side = (
            up_win["blockMode"] == "opposite" and down_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    @staticmethod
    def _check_left_diagonal_win(
        board: list[list[int]], size: int, current_player: int, position: PositionType
    ):
        up_left_win = CaroWin._check_direction_win(
            board, size, current_player, position, UP_LEFT
        )
        down_right_win = CaroWin._check_direction_win(
            board, size, current_player, position, DOWN_RIGHT
        )
        total_pieces = up_left_win["counter"] + down_right_win["counter"]
        is_block_two_side = (
            up_left_win["blockMode"] == "opposite"
            and down_right_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    @staticmethod
    def _check_right_diagonal_win(
        board: list[list[int]], size: int, current_player: int, position: PositionType
    ):
        up_right_win = CaroWin._check_direction_win(
            board, size, current_player, position, UP_RIGHT
        )
        down_left_win = CaroWin._check_direction_win(
            board, size, current_player, position, DOWN_LEFT
        )
        total_pieces = up_right_win["counter"] + down_left_win["counter"]
        is_block_two_side = (
            up_right_win["blockMode"] == "opposite"
            and down_left_win["blockMode"] == "opposite"
        )
        return total_pieces >= 4 and (not is_block_two_side)

    @staticmethod
    def check_win(
        board: list[list[int]], size: int, current_player: int, position: PositionType
    ):
        print(size, current_player)
        counter = 0
        if CaroWin._check_horizontal_win(board, size, current_player, position):
            counter = counter + 1
        if CaroWin._check_vertical_win(board, size, current_player, position):
            counter = counter + 1
        if CaroWin._check_left_diagonal_win(board, size, current_player, position):
            counter = counter + 1
        if CaroWin._check_right_diagonal_win(board, size, current_player, position):
            counter = counter + 1
        return counter
