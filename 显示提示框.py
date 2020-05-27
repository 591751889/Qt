import sys

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QToolTip.setFont(QFont('隶书', 40))

    w = QWidget()
    w.setWindowTitle('编程')

    app.setWindowIcon(QIcon('image/二次陈列.png'))
    w.setToolTip("编程创造城市")
    btn = QPushButton("老刘", w)
    btn.move(50, 50)
    btn.setToolTip('您好，按钮')
    w.resize(600, 800)
    w.show()
    app.exec_()
