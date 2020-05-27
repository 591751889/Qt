import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

from PyQt5.QtGui import QPixmap


class Myclass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 800)
        self.setWindowTitle('编程')
        self.lbl = QLabel('图片展示', self)
        self.lbl.move(200, 200)
        self.lbl.setPixmap(QPixmap('image/二次陈列.png'))
        self.lbl.setScaledContents(True)  # 设置尺寸自适应
        self.lbl.resize(80, 80)  # 直接使用会剪裁

        btn1 = QPushButton('增加图片', self)
        btn2 = QPushButton("删除图片", self)
        btn2.move(0, 100)

        btn2.clicked.connect(self.removePic)
        btn1.clicked.connect(self.addPic)

        self.show()

    def addPic(self):
        self.lbl.setPixmap(QPixmap('image/二次陈列.png'))

    def removePic(self):
        self.lbl.setPixmap(QPixmap(''))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mc = Myclass()

    app.exec_()
