import sys


from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox,QFrame


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("编程")
        self.resize(600,800)
        myFrame=QFrame(self)
        self.cb1=QCheckBox('dance',myFrame)
        self.cb1.stateChanged[int].connect(self.mychange)
        self.cb2=QCheckBox('sing',myFrame)
        self.cb2.stateChanged[int].connect(self.mychange)
        self.cb2.move(0,30)
        myFrame.move(100,100)


        self.show()
    def mychange(self,a):
        print(a)
        b=self.sender()
        print(b.text())



if __name__ == '__main__':
    app=QApplication(sys.argv)
    mc=MyClass()

    app.exec_()