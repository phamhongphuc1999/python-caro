from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QRect

class CaroUIBoard(QWidget):
  size: int

  def __init__(self, size=5):
    super().__init__()
    self.size = size
    self.cell_size = 100
    self.board = [["" for _ in range(size)] for _ in range(size)]
    self.current_player = "X"

    self.setFixedSize(self.size*self.cell_size, self.size*self.cell_size)
    self.setWindowTitle("Caro Game - PyQt6")

  def paintEvent(self, event):
    painter = QPainter(self)
    pen = QPen(Qt.GlobalColor.black, 2)
    painter.setPen(pen)

    for i in range(1, self.size):
      painter.drawLine(0, i*self.cell_size, self.width(), i*self.cell_size)
      painter.drawLine(i*self.cell_size, 0, i*self.cell_size, self.height())

    # vẽ X và O
    for row in range(self.size):
      for col in range(self.size):
        x = col * self.cell_size
        y = row * self.cell_size
        if self.board[row][col] == "X":
          painter.drawLine(x+10, y+10, x+self.cell_size-10, y+self.cell_size-10)
          painter.drawLine(x+self.cell_size-10, y+10, x+10, y+self.cell_size-10)
        elif self.board[row][col] == "O":
          painter.drawEllipse(x+10, y+10, self.cell_size-20, self.cell_size-20)

  def mousePressEvent(self, event):
    col = event.position().x() // self.cell_size
    row = event.position().y() // self.cell_size

    if self.board[int(row)][int(col)] == "":
      self.board[int(row)][int(col)] = self.current_player
      # if self.check_win(int(row), int(col)):
      #   print(f"{self.current_player} wins!")
      #   self.reset_board()
      # else:
      #   self.current_player = "O" if self.current_player == "X" else "X"
      self.current_player = "O" if self.current_player == "X" else "X"

    self.update()

  def reset_board(self):
    self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
    self.current_player = "X"

def draw_board(size=5):
  app = QApplication([])
  window = CaroUIBoard(size)
  window.show()
  app.exec()
