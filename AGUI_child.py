from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class Ui_childWindow(QWidget):
    def __init__(self):
        super(Ui_childWindow, self).__init__()


    def setupUi(self, childWindow):
        self.center()
        childWindow.setObjectName("childWindow")
        childWindow.resize(580, 650)
        childWindow.setStyleSheet("#childWindow{background-color: lightgray}")
        childWindow.setWindowFlags(Qt.FramelessWindowHint)
        #图片显示框
        self.View = QtWidgets.QLabel(self)
        self.View.setGeometry(20, 10, 540, 485)
        lena = cv2.imread("lena.jpg")
        lena = cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = lena.shape
        bytesPerLine = bytesPerComponent * width
        lena_image = QImage(lena.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.View.setPixmap(QPixmap.fromImage(lena_image).scaled(self.View.width(), self.View.height()))


        #信息显示框（两层嵌套，frame与VBox）
        self.frame = QtWidgets.QFrame(childWindow)
        self.frame.setGeometry(QtCore.QRect(400, 520, 245, 115))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.listView_1 = QtWidgets.QLabel(self.frame)
        self.listView_1.setGeometry(QtCore.QRect(90, 10, 91, 21))
        self.listView_1.setObjectName("listView_1")
        self.listView_2 = QtWidgets.QLabel(self.frame)
        self.listView_2.setGeometry(QtCore.QRect(90, 50, 91, 21))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QLabel(self.frame)
        self.listView_3.setGeometry(QtCore.QRect(90, 90, 91, 21))
        self.listView_3.setObjectName("listView_3")       

        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 90, 100))
        self.layoutWidget.setObjectName("layoutWidget")

        self.VBox = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.VBox.setContentsMargins(0, 0, 0, 0)
        self.VBox.setObjectName("VBox")

        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setObjectName("label_1")
        self.VBox.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.VBox.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.VBox.addWidget(self.label_3)
        #选择按钮
        self.pushButton_1 = QtWidgets.QPushButton(childWindow)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 510, 60, 60))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(childWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 510, 60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(childWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 585, 60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(childWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 585, 60, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        #提醒模式选择
        self.label = QtWidgets.QLabel(childWindow)
        self.label.setGeometry(QtCore.QRect(200, 510, 180, 25))
        self.label.setObjectName("label")
        self.radioButton_1 = QtWidgets.QRadioButton(childWindow)
        self.radioButton_1.setGeometry(QtCore.QRect(240, 550, 71, 16))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(childWindow)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 580, 71, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(childWindow)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 610, 59, 16))
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(childWindow)
        QtCore.QMetaObject.connectSlotsByName(childWindow)


        # 美化
        self.setWindowOpacity(0.9)
        self.pushButton_1.setStyleSheet('''QPushButton{background:#F7D674;border-radius:30px;}
                QPushButton:hoVBox{background:wheat;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:30px;}
                QPushButton:hoVBox{background:wheat;}''')
        self.pushButton_3.setStyleSheet('''QPushButton{background:#F7D674;border-radius:30px;}
                QPushButton:hoVBox{background:wheat;}''')
        self.pushButton_4.setStyleSheet('''QPushButton{background:#F7D674;border-radius:30px;}
                QPushButton:hoVBox{background:wheat;}''')
        self.label.setStyleSheet('''QLabel{color:dark;background:white;border:2px solid #F3F3F5;border-radius:45px;
                        font-size:14pt; font-weight:400;font-family: Roman times;} ''')
        self.label_1.setStyleSheet('''QLabel{color:black;border:2px; font-size:15px;font-family:华文彩云;}''')
        self.label_2.setStyleSheet('''QLabel{color:black;border:2px; font-size:15px;font-family:华文彩云;}''')
        self.label_3.setStyleSheet('''QLabel{color:black;border:2px; font-size:15px;font-family:华文彩云;}''')

        self.listView_1.setStyleSheet('''QLabel{color:black;font-size:12px;font-family:Roman times;}''')
        self.listView_2.setStyleSheet('''QLabel{color:black;font-size:12px;font-family:Roman times;}''')
        self.listView_3.setStyleSheet('''QLabel{color:black;font-size:12px;font-family:Roman times;}''')


    def retranslateUi(self, childWindow):
        _translate = QtCore.QCoreApplication.translate
        childWindow.setWindowTitle(_translate("childWindow", "眨眼宝"))
        self.label_1.setText(_translate("childWindow", "眨眼频率："))
        self.label_2.setText(_translate("childWindow", "眨眼次数："))
        self.label_3.setText(_translate("childWindow", "距上次眨眼："))
        self.pushButton_1.setText(_translate("childWindow", "运行(&R)"))
        self.pushButton_2.setText(_translate("childWindow", "暂停(&P)"))
        self.pushButton_3.setText(_translate("childWindow", "最小化(&M)"))
        self.pushButton_4.setText(_translate("childWindow", "托盘化(&T)"))
        self.label.setText(_translate("childWindow", "眨眼提醒模式选择："))
        self.radioButton_1.setText(_translate("childWindow", "语音提醒"))
        self.radioButton_2.setText(_translate("childWindow", "文字提醒"))
        self.radioButton_3.setText(_translate("childWindow", "无提醒"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/4)