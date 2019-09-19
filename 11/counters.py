from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Counters(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.rect = [[0] * 3 for i in range(3)]
        self.select = [0, 0]
        self.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))
        self.setMinimumSize(self.minimumSizeHint())

    def minimumSizeHint(self):
        return QSize(116, 100)

    def mousePressEvent(self, event=None):
        if event.button() == Qt.LeftButton:
            self.selectEllipse(event.x(), event.y())
            event.accept()
        else:
            QWidget.mousePressEvent(self, event)

    def selectEllipse(self, mx, my):
        x = mx / self.width()
        y = my / self.height()

        if 0 <= x < (1 / 3.0):
            x = 0
        elif (1 / 3.0) <= x < (2 / 3.0):
            x = 1
        else:
            x = 2

        if 0 <= y < (1 / 3.0):
            y = 0
        elif (1 / 3.0) <= y < (2 / 3.0):
            y = 1
        else:
            y = 2

        self.rect[x][y] += 1
        if self.rect[x][y] == 3:
            self.rect[x][y] = 0

        self.select = [x, y]

        self.update()

    def keyPressEvent(self, event=None):
        changex = changey = 0
        if event.key() == Qt.Key_Left:
            changex = - 1
        elif event.key() == Qt.Key_Right:
            changex = 1
        elif event.key() == Qt.Key_Up:
            changey = - 1
        elif event.key() == Qt.Key_Down:
            changey = 1
        if changex or changey:
            self.select[0] += changex
            if self.select[0] == 3:
                self.select[0] = 0
            elif self.select[0] == -1:
                self.select[0] = 2
            self.select[1] += changey
            if self.select[1] == 3:
                self.select[1] = 0
            elif self.select[1] == -1:
                self.select[1] = 2
            self.update()
            event.accept()
        if event.key() == Qt.Key_Space:
            x = self.select[0]
            y = self.select[1]
            self.rect[x][y] += 1
            if self.rect[x][y] == 3:
                self.rect[x][y] = 0
            self.update()
            event.accept()
        else:
            QWidget.keyPressEvent(self, event)

    def paintEvent(self, event=None):
        sWidth  = (1 / 3.0) * self.width()
        sHeight = (1 / 3.0) * self.height()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.black)

        for i in range(0, 3):
            for j in range(0, 3):
                painter.save()
                painter.drawRect(i * sWidth, j * sHeight, sWidth, sHeight)
                painter.setPen(QPen(Qt.blue, 3))
                painter.drawRect(self.select[0] * sWidth, self.select[1] * sHeight, sWidth, sHeight)
                if self.rect[i][j] == 1:
                    painter.setPen(Qt.black)
                    painter.setBrush(QBrush(Qt.yellow))
                    painter.drawEllipse(i * sWidth, j * sHeight, sWidth, sHeight)
                elif self.rect[i][j] == 2:
                    painter.setPen(Qt.black)
                    painter.setBrush(QBrush(Qt.red))
                    painter.drawEllipse(i * sWidth, j * sHeight, sWidth, sHeight)
                painter.restore()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = Counters()
    form.setWindowTitle("Counters")
    form.show()
    form.resize(200, 200)
    app.exec_()