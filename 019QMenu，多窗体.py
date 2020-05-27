import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QAction, QMessageBox


class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('????')
        self.resize(600, 600)

        menubar = self.menuBar()
        filemenu=menubar.addMenu('文件')

        actionNewWIn=QAction('新建窗体',self)
        actionNewWIn.triggered.connect(self.MyNewwin)
        filemenu.addAction(actionNewWIn)
        filemenu.addAction("新建")
        small=filemenu.addMenu('最近的')
        small.addAction('1')
        small.addAction('2')
        small.addAction('3')

        menubar.addAction('运行')

        menubar.addAction('调试')
        actHelp = QAction('帮助', self)
        actHelp.triggered.connect(self.help)
        menubar.addAction(actHelp)

        self.show()

    def help(self):
        messagebox = QMessageBox.question(self, 'help', '欢迎添加微信', QMessageBox.Ok)
        # messagebox.show()
    def MyNewwin(self):
        mc=MyClass2()

class MyClass2(QWidget):
    def __init__(self):
        super(MyClass2, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('111')

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()
