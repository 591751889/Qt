import sys

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("编程")
# w.setWindowIcon(QIcon('image/二次陈列.png'))xuex
w.show()
app.setWindowIcon(QIcon('image/二次陈列.png'))
sys.exit(app.exec_())
