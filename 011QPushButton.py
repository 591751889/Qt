import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QFrame, QApplication, QPushButton, QVBoxLayout, QHBoxLayout


class MyClass(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("编程")
        self.resize(800, 600)

        self.color = QColor(0, 0, 0)
        btnREd = QPushButton('红')
        btnGreen = QPushButton('绿')
        btnBlue = QPushButton('蓝')

        btnREd.setCheckable(True)
        btnGreen.setCheckable(True)
        btnBlue.setCheckable(True)

        btnREd.clicked[bool].connect(self.setColor)
        btnGreen.clicked[bool].connect(self.setColor)
        btnBlue.clicked[bool].connect(self.setColor)

        vLo = QVBoxLayout()
        vLo.addWidget(btnREd)
        vLo.addWidget(btnGreen)
        vLo.addWidget(btnBlue)

        self.myFrame = QFrame()
        self.myFrame.setWindowIconText("1111")
        # self.myFrame.setStyleSheet('QFrame{background-color: black}')
        self.myFrame.setStyleSheet('QFrame{background-color: %s}' % self.color.name())

        hlo = QHBoxLayout(self)
        hlo.addLayout(vLo)
        hlo.addWidget(self.myFrame)

        self.show()

    def setColor(self, p):
        # print(p)

        b = self.sender()
        if p:
            v = 255
        else:
            v = 0
        if b.text()=="红":
            self.color.setRed(v)
            print(self.color.name())
        elif b.text()=='绿':
            self.color.setGreen(v)

        elif b.text()=='蓝':
            self.color.setBlue(v)
        self.myFrame.setStyleSheet('QFrame{background-color: %s}' % self.color.name())





if __name__ == '__main__':
    app = QApplication(sys.argv)

    mc = MyClass()
    app.exec_()
