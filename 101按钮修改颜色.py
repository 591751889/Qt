import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QColor

class Example(QWidget):

  def __init__(self):
    super().__init__()

    self.initUI()

  def initUI(self):

    self.col = QColor(0, 0, 0)

    redb = QPushButton('红', self)
    redb.setCheckable(True)
    redb.move(10, 10)

    greenb = QPushButton('绿', self)
    greenb.setCheckable(True)
    greenb.move(10, 60)

    blueb = QPushButton('蓝', self)
    blueb.setCheckable(True)
    blueb.move(10, 110)

    redb.clicked[bool].connect(self.setColor)
    greenb.clicked[bool].connect(self.setColor)
    blueb.clicked[bool].connect(self.setColor)

    self.square = QFrame(self)
    self.square.setGeometry(150, 20, 100, 100)
    self.square.setStyleSheet('QWidget { background-color:%s }' %
      self.col.name())
    # print()

    self.setGeometry(300, 300, 280, 170)
    self.setWindowTitle('切换按钮')
    self.show()

  def setColor(self, pressed):

    source = self.sender()

    if pressed:
      val = 255
    else:
      val = 0

    if source.text() == '红':
      self.col.setRed(val)
      print(self.col.name())
    elif source.text() == '绿':
      self.col.setGreen(val)
    else:
      self.col.setBlue(val)

    self.square.setStyleSheet('QFrame { background-color:%s }' %
      self.col.name())

if __name__ == '__main__':

  app = QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())