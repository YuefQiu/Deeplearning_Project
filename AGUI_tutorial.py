# -*- coding: utf-8 -*-

# Tutorial implementation generated from reading ui file 'AGUI_introduction.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tutorial(QWidget):
    def __init__(self):
        super(Ui_Tutorial, self).__init__()
        self.setupUi(self)
        
    def setupUi(self, Tutorial):
        self.setWindowIcon(QIcon('eye.jpg'))
        Tutorial.setWindowFlags(Qt.WindowStaysOnTopHint)
        Tutorial.setObjectName("Tutorial")
        Tutorial.setFixedSize(300, 250)
        self.textBrowser = QtWidgets.QTextBrowser(Tutorial)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 300, 250))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Tutorial)
        QtCore.QMetaObject.connectSlotsByName(Tutorial)

    def retranslateUi(self, Tutorial):
        _translate = QtCore.QCoreApplication.translate
        Tutorial.setWindowTitle(_translate("Tutorial", "Tutorial"))
        self.textBrowser.setHtml(_translate("Tutorial", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">            使用指南：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  1.执行exe文件</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  2.等待启动界面加载完成</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  3.点击‘start’进入运行窗口or‘leave’关闭程序</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  4.四个按钮可执行各自任务（快捷键为Alt+字母）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  5.最小化/托盘化后，程序仍在执行,若需退出，请通过托盘退出</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  6.请注意托盘处操作</span></p></body></html>"))

import pic_rc
