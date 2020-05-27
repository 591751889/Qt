import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication

from my_ui import test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    mainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    sys.exit(app.exec_())
