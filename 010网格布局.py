import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit, QLabel, QGridLayout, QHBoxLayout
from PyQt5 import QtCore



class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("编程")
        self.setGeometry(1100, 200, 400, 300)
        # self.setGeometry(QtCore.QRect(300, 200, 400, 300))
        lbtitle = QLabel("标题")
        lbauthor = QLabel("作者")
        lbcontent = QLabel('正文')

        letitle = QLineEdit()
        leauthor = QLineEdit()
        lecontent = QTextEdit()

        grid = QGridLayout(self)
        grid.setSpacing(20)
        grid.addWidget(lbtitle, 0, 0)
        grid.addWidget(letitle, 0, 1)
        grid.addWidget(lbauthor, 1, 0)
        grid.addWidget(leauthor, 1, 1)
        grid.addWidget(lbcontent, 2, 0)
        grid.addWidget(lecontent, 2, 1)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()
