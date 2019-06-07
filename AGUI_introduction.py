from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets


class Ui_Introduction(QWidget):
    def __init__(self):
        super(Ui_Introduction, self).__init__()
        self.setupUi(self)

    def setupUi(self, Introduction):
        self.setWindowIcon(QIcon('eye.jpg'))
        Introduction.setWindowFlags(Qt.WindowStaysOnTopHint)
        Introduction.setObjectName("Introduction")
        Introduction.setFixedSize(300, 250)
        self.textBrowser = QtWidgets.QTextBrowser(Introduction)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 300, 250))
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(Introduction)
        QtCore.QMetaObject.connectSlotsByName(Introduction)

    def retranslateUi(self, Introduction):
        _translate = QtCore.QCoreApplication.translate
        Introduction.setWindowTitle(_translate("Introduction", "Introduction"))
        self.textBrowser.setHtml(_translate("Introduction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">             产品介绍：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />  <span style=\" font-size:10pt;\">本产品——“护眼宝”——由邱岳峰、石致远、王铭浩和陈一龙共同开发，旨在帮助电脑使用人员健康护眼。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  “护眼宝”界面简练，操作方便，功能齐全。以“深度学习”中的二分类网络为核心模型，且占用系统资源少，可谓效果效率两开花。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  如您第一次使用本产品，请参考“使用指南”。</span></p></body></html>"))

