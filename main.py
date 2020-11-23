import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint
from UI import Ui_Form

SCREEN_SIZE = (696, 501)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.drawing = False
        self.pushButton.clicked.connect(self.draw_start)

    def draw_start(self):
        self.x = randint(0, SCREEN_SIZE[0])
        self.y = randint(0, SCREEN_SIZE[1])
        self.d = randint(10, 100)
        self.r, self.g, self.b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.drawing = True

    def paintEvent(self, event):
        if self.drawing:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(self.r, self.g, self.b))
            qp.drawEllipse(self.x, self.y, self.d, self.d)
            qp.end()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Window()
    wind.show()
    sys.exit(app.exec())
