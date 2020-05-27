import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 color dialog - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open color dialog', self)
        button.setToolTip('Opens color dialog')
        button.move(10, 10)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        qp = QPainter(self)
        color = QColorDialog.getColor()

        if color.isValid():
            # 实例化调色板
            palette1 = QtGui.QPalette()
            # 设置调色板颜色
            palette1.setColor(palette1.Background, color)
            # 应用调色板
            self.setPalette(palette1)
            print(color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())