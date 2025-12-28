from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QRect

from CaroBoard import CaroBoard


class CaroUIBoard(QWidget):

    def __init__(self, size=5):
        super().__init__()
        self.board = CaroBoard(size)
        self.cell_size = 100

        _size = self.board.size * self.cell_size
        self.setFixedSize(_size, _size)
        self.setWindowTitle("Caro Game - PyQt6")

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.black, 2)
        painter.setPen(pen)

        for i in range(1, self.board.size):
            painter.drawLine(0, i * self.cell_size, self.width(), i * self.cell_size)
            painter.drawLine(i * self.cell_size, 0, i * self.cell_size, self.height())

        for row in range(self.board.size):
            for col in range(self.board.size):
                x = col * self.cell_size
                y = row * self.cell_size
                if self.board.board[row][col] == 1:
                    painter.drawLine(
                        x + 10, y + 10, x + self.cell_size - 10, y + self.cell_size - 10
                    )
                    painter.drawLine(
                        x + self.cell_size - 10, y + 10, x + 10, y + self.cell_size - 10
                    )
                elif self.board.board[row][col] == 2:
                    painter.drawEllipse(
                        x + 10, y + 10, self.cell_size - 20, self.cell_size - 20
                    )

    def mousePressEvent(self, event):
        col = event.position().x() // self.cell_size
        row = event.position().y() // self.cell_size

        if self.board.board[int(row)][int(col)] == 0:
            self.board.board[int(row)][int(col)] = self.board.current_player
            if self.board.move([int(row), int(col)]):
                print("Player ", self.board.current_player, " won!")
                self.reset_board()

        self.update()
        self.board.draw()

    def reset_board(self):
        self.board.reset()


def draw_board(size=5):
    app = QApplication([])
    window = CaroUIBoard(size)
    window.show()
    app.exec()
