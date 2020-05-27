import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSlider
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('编程')
        self.resize(600, 600)
        sl = QSlider(Qt.Horizontal, self)
        sl.setMinimum(0)
        sl.setMaximum(255)
        sl.valueChanged[int].connect(self.change)

        sl.move(50, 50)
        self.show()

    def change(self, a):
        
        self.setColor(a)
        # print(a)

    def setColor(self, a):
        mycolor = QColor(0, 0, 0)
        mycolor.setBlue(a)
        self.setStyleSheet("QWidget{background-color:%s}"%mycolor.name())

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()

    app.exec_()
