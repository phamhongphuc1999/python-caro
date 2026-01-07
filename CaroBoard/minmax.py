from CaroBoard.caro_win import CaroWin
from CaroBoard.evaluation import Evaluation
from CaroBoard.utils import is_in_board
from type import EMPTY, PositionType
from typing import Set
import math


class MinmaxUtils:
    @staticmethod
    def generate_candidate_moves(board: list[list[int]], radius=2):
        moves: Set[PositionType] = set()
        size = len(board)
        for x in range(size):
            for y in range(size):
                if board[x][y] != EMPTY:
                    continue
                for dx in range(-radius, radius + 1):
                    for dy in range(-radius, radius + 1):
                        nx, ny = x + dx, y + dy
                        if (is_in_board(nx, ny, size)) and board[nx][ny] != EMPTY:
                            moves.add((x, y))
                            break
        return moves

    @staticmethod
    def order_moves(board: list[list[int]], moves: Set[PositionType], player: int):
        scored = []

        for move in moves:
            x, y = move
            board[x][y] = player
            score = Evaluation.heuristic(board, player)
            board[x][y] = 0
            scored.append((score, move))

        scored.sort(reverse=True)
        return [m for _, m in scored]

    @staticmethod
    def make_move(board: list[list[int]], move: PositionType, player: int):
        x, y = move
        board[x][y] = player

    @staticmethod
    def undo_move(board: list[list[int]], move: PositionType):
        x, y = move
        board[x][y] = EMPTY

    @staticmethod
    def minmax(
        board: list[list[int]],
        current_player: int,
        move: PositionType,
        depth: int,
        alpha: int,
        beta: int,
        is_max: bool,
    ):
        if depth == 0 or CaroWin.check_win(board, len(board), current_player, move):
            return Evaluation.heuristic(board, current_player)
        moves = MinmaxUtils.generate_candidate_moves(board)
        moves = MinmaxUtils.order_moves(board, moves)
        if is_max:
            value = -math.inf
            for move in moves:
                MinmaxUtils.make_move(board, move, current_player)
                value = max(
                    value,
                    MinmaxUtils.minimax(
                        board, 3 - current_player, move, depth - 1, alpha, beta, False
                    ),
                )
                MinmaxUtils.undo_move(board, move)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = math.inf
            for move in moves:
                MinmaxUtils.make_move(board, move, current_player)
                value = min(
                    value,
                    MinmaxUtils.minimax(
                        board, 3 - current_player, move, depth - 1, alpha, beta, True
                    ),
                )
                MinmaxUtils.undo_move(board, move)

                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value
