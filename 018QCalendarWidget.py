import sys

from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1600, 600)
        self.setWindowTitle("日历控件")

        vlo = QVBoxLayout(self)
        self.lbl = QLabel('这里显示日期')
        self.lbl.setFont(QFont('', 20))
        cal = QCalendarWidget(self)

        vlo.addWidget(cal)
        vlo.addWidget(self.lbl)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mc = MyClass()

    app.exec_()
