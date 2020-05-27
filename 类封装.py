import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # print('1')
        self.setWindowTitle('编程')
        self.resize(300, 200)
        btn = QPushButton("我是一个按钮", self)
        btn.move(20, 50)
        btn.clicked.connect(self.close)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()
