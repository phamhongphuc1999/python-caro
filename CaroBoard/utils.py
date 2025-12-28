from type import EMPTY, PositionType


def generate_moves(board: list[list[int]], size: int) -> list[PositionType]:
    moves = set()
    for row in range(size):
        for column in range(size):
            if board[row][column] == EMPTY:
                moves.add([row, column])
    return list(moves)
