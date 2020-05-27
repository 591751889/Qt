import sys

from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("编程")
        self.resize(600,600)
        self.lbl=QLabel("显示区",self)
        self.lbl.move(50,50)

        le=QLineEdit(self)
        le.textChanged[str].connect(self.shouTExt)
        self.show()

    def shouTExt(self,s):
        self.lbl.setText(s)
        self.lbl.adjustSize()
        print(s)



if __name__ == '__main__':
    app=QApplication(sys.argv)

    mc=MyClass()




    app.exec_()