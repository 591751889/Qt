
import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QApplication,QLabel


class TableView(QWidget):

    def __init__(self, arg=None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle("QTableView表格视图控件演示")
        self.resize(500, 300)
        self.label=QLabel()
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])

        self.tableview = QTableView()
        # 关联QTableView控件和Model
        self.tableview.setModel(self.model)

        # 添加数据
        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        item31 = QStandardItem('30')
        item32 = QStandardItem('死亡女神')
        item33 = QStandardItem('3000')
        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)


        # layout = QVBoxLayout()
        # layout.addWidget(self.tableview)
        #
        # self.setLayout(layout)
        # self.addW


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = TableView()
    table.show()
    sys.exit(app.exec_())
