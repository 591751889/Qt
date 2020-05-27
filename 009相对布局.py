import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit,QLabel,QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("编程")
        self.resize(600,600)
        lecode=QLineEdit(self)
        label=QLabel("验证码",self)
        btn=QPushButton("验证",self)
        # lecode.move(40,0)
        # btn.move(180,0)
        hlayout=QHBoxLayout(self)
        hlayout.addWidget(lecode)
        hlayout.addStretch(1)
        hlayout.addWidget(label)
        hlayout.addStretch(1)
        hlayout.addWidget(btn)

        hlayout.addStretch(1)

        vlayout=QVBoxLayout(self)
        vlayout.addLayout(hlayout)
        vlayout.addStretch()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mc = MyClass()

    app.exec_()
