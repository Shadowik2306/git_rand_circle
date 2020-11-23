import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from random import randint

SCREEN_SIZE = (696, 501)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.drawing = False
        self.pushButton.clicked.connect(self.draw_start)

    def draw_start(self):
        self.x = randint(0, SCREEN_SIZE[0])
        self.y = randint(0, SCREEN_SIZE[1])
        self.drawing = True

    def paintEvent(self, event):
        if self.drawing:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 211, 0))
            qp.drawEllipse(self.x, self.y, 50, 50)
            qp.end()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Window()
    wind.show()
    sys.exit(app.exec())
