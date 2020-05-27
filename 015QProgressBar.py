import sys

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('编程')
        self.resize(600,600)

        self.progress=0
        self.timer=QBasicTimer()
        self.progressbar=QProgressBar(self)
        self.progressbar.move(50,50)
        self.progressbar.setMaximum(100)
        self.progressbar.setMinimum(0)

        self.progressbar.setValue(self.progress)

        self.btn=QPushButton("bigin",self)
        self.btn.move(100,100)
        self.btn.clicked.connect(self.changeProgress)

        self.show()

    def changeProgress(self):
        if self.timer.isActive():
            # self.timer.start(100)
            self.timer.stop()
            self.btn.setText('开始')

        else:
            self.timer.start(100, self)
            self.btn.setText('停止')
    def timerEvent(self, a0: 'QTimerEvent'):
        self.progress+=1
        self.progressbar.setValue(self.progress)
        if self.progress==100:
            self.changeProgress()
        # print('编程')





if __name__ == '__main__':
    app=QApplication(sys.argv)

    mc=MyClass()

    app.exec_()