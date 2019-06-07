from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fatherWindow(QWidget):
    def __init__(self):
        super(Ui_fatherWindow, self).__init__()

    def setupUi(self, fatherWindow):
        self.center()
        fatherWindow.setObjectName("fatherWindow")
        fatherWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        fatherWindow.setStyleSheet("#fatherWindow{background-color: lightgreen}")
        self.setWindowIcon(QIcon('eye.jpg'))
        fatherWindow.setFixedSize(215, 75)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        fatherWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(fatherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 20, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 16, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(120, 20, 75, 30))
        self.exit.setObjectName("exit")
        self.exit.setFont(font)
        fatherWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(fatherWindow)
        QtCore.QMetaObject.connectSlotsByName(fatherWindow)
        self.start.clicked.connect(fatherWindow.close)
        self.exit.clicked.connect(qApp.quit)
        #美化
        self.setWindowOpacity(0.9)

    def retranslateUi(self, fatherWindow):
        _translate = QtCore.QCoreApplication.translate
        fatherWindow.setWindowTitle(_translate("fatherWindow", "眨眼宝"))
        self.start.setText(_translate("mainWindow", "start"))
        self.exit.setText(_translate("mainWindow", "leave"))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

