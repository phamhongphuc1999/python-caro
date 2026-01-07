from CaroBoard.caro_win import CaroWin
from CaroBoard.utils import draw_list
from type import EMPTY, PLAYER1, PositionType


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

    def _switch_current_player(self):
        self.current_player = 3 - self.current_player
        return self.current_player

    def move(self, position: PositionType):
        self.board[position[0]][position[1]] = self.current_player
        if CaroWin.check_win(self.board, self.size, self.current_player, position):
            return True
        self._switch_current_player()
        return False

    def draw(self):
        draw_list(self.board, self.size)

    def reset(self):
        self.current_player = PLAYER1
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
