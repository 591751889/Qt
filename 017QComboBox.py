import sys

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QFrame


class MyClass(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("program")
        self.resize(600, 800)

        frame = QFrame(self)
        lbl = QLabel('省', frame)

        combobox1 = QComboBox(frame)
        combobox1.move(30, 0)
        self.combobox2 = QComboBox(frame)
        self.combobox2.move(30, 30)

        # combobox1.addItem('浙江')
        # combobox1.addItem('江苏')
        # combobox1.addItem('安徽')
        provice = ['浙江', '江苏', '安徽']
        combobox1.addItems(provice)
        #############################################################################
        combobox1.setEditable(True)

###################################################################################
        lbl = QLabel('市', frame)
        lbl.move(0, 30)
        city = ['浙江', '江苏', '安徽']
        # combobox2.addItems(provice)
        # combobox1.activated[str].connect(self.showCity)
        combobox1.activated[int].connect(self.showCity)
        self.show()

    def showCity(self, p):
        print(p)
        city=[
            ['浙江1', '浙江2', '浙江3'],
         ['江苏1', '江苏2', '江苏3'],
         ['安徽1', '安徽2', '安徽3']]
        self.combobox2.clear()
        self.combobox2.addItems(city[p])



if __name__ == '__main__':
    app = QApplication(sys.argv)

    mc = MyClass()

    app.exec_()


