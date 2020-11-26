from PyQt5 import QtCore, QtWidgets
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Ui_Product(object):
    def setupUi(self, Product):
        Product.setObjectName("Product")
        Product.resize(537, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Product.sizePolicy().hasHeightForWidth())
        Product.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Product)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 71, 51))
        self.pushButton.setObjectName("pushButton")
        Product.setCentralWidget(self.centralwidget)

        self.retranslateUi(Product)
        QtCore.QMetaObject.connectSlotsByName(Product)

    def retranslateUi(self, Product):
        _translate = QtCore.QCoreApplication.translate
        Product.setWindowTitle(_translate("Product", "MainWindow"))
        self.pushButton.setText(_translate("Product", "Круг"))


class MyWidget(QMainWindow, Ui_Product):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.ff)

    def paint(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.flag = False
        for i in range(10):
            self.qp.setBrush(QColor(random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)))
            self.coords = [random.randint(10, 500), random.randint(10, 500)]
            v = random.randint(10, 500)
            self.qp.drawEllipse(*self.coords, v, v)

    def ff(self, event):
        self.paint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

