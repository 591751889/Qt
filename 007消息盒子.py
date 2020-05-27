import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def closeEvent(self, QCloseEvent):
        # print('???')
        print(type(self))
        result = QMessageBox.question(self, "提示", '您真的要关闭窗体嘛', QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            print("谢谢")
            QCloseEvent.ignore()
            QMessageBox.information(self, "消息", "谢谢！")

    def initUI(self):
        self.move(300,300)
        self.setWindowTitle("消息盒子的学习")
        btn = QPushButton("我是一个按钮", self)
        btn.clicked.connect(self.close)
        self.resize(600, 800)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()
