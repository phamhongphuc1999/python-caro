class CaroBoard:
  size: int
  current_player: int
  board: list[list[int]]

  def __init__(self, size=5):
    self.size = size
    self.current_player = 1
    self.board = [[0 for _ in range(size)] for _ in range(size)]

  def _check_win(self):
    return False

  def _switch_current_player(self):
    self.current_player = 3 - self.current_player
    return self.current_player
  
  def move(self, row: int, column: int):
    self.board[row][column] = self.current_player
    if self._check_win():
      return True
    self._switch_current_player()
    return False
  
  def draw(self):
    print('***************************')
    for row in range(self.size):
      for _ in range(2*self.size):
        print(end="-")
      print()
      for column in range(self.size):
        print(self.board[row][column], end="|")
      print()
    print('***************************')

  def reset(self):
    self.current_player = 0
    self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
