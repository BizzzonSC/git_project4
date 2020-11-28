import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        con = sqlite3.connect('coffe.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Coffe""")
        r1 = ''
        for elem in result:
            r = ''
            for i in elem:
                t = str(i)
                r += t
                r += ', '
            r = r[:-2]
            r1 += r + '\n'
        r1 = r1[:-2]
        self.textEdit.append(r1)
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())