from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QGridLayout, QToolButton
from gevent.libev.corecext import SIGNAL


class Geometry(QDialog):
    def __init__ (self):
        QDialog.__init__(self)
        self.frame=1
        layout=QGridLayout(self)
        btnAbout=QToolButton()
        btnAbout.setText('About Qt')
        btnAbout.setIcon(QIcon('hjz.png'))
        btnAbout.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        layout.addWidget(btnAbout,0,0,Qt.AlignTop|Qt.AlignLeft)

        self.connect(btnAbout,SIGNAL('clicked()'),self.slotAbout)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(300,200)
        # self.show()
        self.hide()

    def slotAbout(self):
        QMessageBox.aboutQt(self)
    def enterEvent(self, evt):
        self.activateWindow()
        if(self.x() == self.frame-self.width()):
            self.move(-self.frame,self.y())
        elif(self.y() == self.frame-self.height()+self.y()-self.geometry().y()):
            self.move(self.x(),-self.frame)
    def leaveEvent(self,evt):
        cx,cy=QCursor.pos().x(),QCursor.pos().y()
        if(cx >= self.x() and cx <= self.x()+self.width()
            and cy >= self.y() and cy <= self.geometry().y()):
            return#title bar
        elif(self.x() < 0 and QCursor.pos().x()>0):
            self.move(self.frame-self.width(),self.y())
        elif(self.y() < 0 and QCursor.pos().y()>0):
            self.move(self.x(), self.frame-self.height()+self.y()-self.geometry().y())

if __name__=='__main__':
    app=QApplication([])
    win=Geometry()
    app.setActiveWindow(win)
    app.exec_()