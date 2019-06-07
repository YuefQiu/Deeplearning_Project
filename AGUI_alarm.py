# -*- coding: utf-8 -*-

# Alarm implementation generated from reading ui file 'AGUI_alarm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets

class Ui_Alarm(QWidget):
    def __init__(self):
        super(Ui_Alarm, self).__init__()
        self.setupUi(self)
        
    def setupUi(self, Alarm):
        self.setWindowIcon(QIcon('eye.jpg'))
        Alarm.setWindowFlags(Qt.WindowStaysOnTopHint)
        Alarm.setObjectName("Alarm")
        Alarm.setFixedSize(300, 35)
        self.message_label = QtWidgets.QLabel(Alarm)
        self.message_label.setGeometry(QtCore.QRect(0, 0, 300, 35))
        self.message_label.setObjectName("label")

        self.retranslateUi(Alarm)
        QtCore.QMetaObject.connectSlotsByName(Alarm)

    def retranslateUi(self, Alarm):
        _translate = QtCore.QCoreApplication.translate
        Alarm.setWindowTitle(_translate("Alarm", "Alarm"))

