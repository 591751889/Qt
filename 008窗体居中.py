import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class MyFormal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("编程")
        lbl = QLabel("编程创造城市！",self)
        self.resize(400,800)
        self.move(50,50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dk=app.desktop()
    print(dk.width())
    mfl = MyFormal()
    mfl.move(100,140)
    app.exec_()
