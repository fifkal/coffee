import sqlite3 as sql
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id кофе', 'сорт',
                                                    'степень прожарки', 'молотый/растворимый', 'вкус',
                                                    'цена', 'объём упаковки'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.con = sql.connect("coffee.db")
        self.cur = self.con.cursor()
        result = self.cur.execute(f"SELECT * FROM coffee").fetchall()
        if result:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in self.cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('pics/icon.png'))
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())

