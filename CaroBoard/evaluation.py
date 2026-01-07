from type import EVALUATION_DIRECTIONS, EVALUATION_SCORES
from CaroBoard.utils import is_in_board


class Evaluation:
    @staticmethod
    def _evaluate_player(board: list[list[int]], player: int):
        score = 0
        size = len(board)
        for x in range(size):
            for y in range(size):
                if board[x][y] != player:
                    continue

                for dx, dy in EVALUATION_DIRECTIONS:
                    # prevent double
                    prev_x, prev_y = x - dx, y - dy
                    if (
                        is_in_board(prev_x, prev_y, size)
                        and board[prev_x][prev_y] == player
                    ):
                        continue

                    length = 0
                    nx, ny = x, y
                    while is_in_board(nx, ny, size) and board[nx][ny] == player:
                        length += 1
                        nx += dx
                        ny += dy

                    # check two heads
                    open_ends = 0

                    # the first head
                    if is_in_board(prev_x, prev_y, size) and board[prev_x][prev_y] == 0:
                        open_ends += 1

                    # the second head
                    if is_in_board(nx, ny, size) and board[nx][ny] == 0:
                        open_ends += 1

                    score += EVALUATION_SCORES.get((length, open_ends), 0)

        return score

    @staticmethod
    def heuristic(board: list[list[int]], current_player: int):
        return Evaluation._evaluate_player(
            board, current_player
        ) - Evaluation._evaluate_player(board, 3 - current_player)
