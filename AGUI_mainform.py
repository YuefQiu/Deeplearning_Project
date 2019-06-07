from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from AGUI_child1 import Ui_childWindow1
from AGUI_father1 import Ui_fatherWindow1
from AGUI_introduction import Ui_Introduction
from AGUI_tutorial import Ui_Tutorial

class MainForm(QMainWindow, Ui_fatherWindow1):
    def __init__(self):
        super(MainForm, self).__init__()
        QApplication.setQuitOnLastWindowClosed(False)
        self.setupUi(self)

        #子窗口实例化
        self.child = Ui_childWindow1()
        #创建托盘程序
        self.tray = QSystemTrayIcon(QIcon('eye.jpg'))  # 创建系统托盘对象
        #创建托盘菜单
        self.tray_menu = QMenu(QApplication.desktop())
        self.tray.setContextMenu(self.tray_menu)
        # 为菜单添加动作
        self.RestoreAction = QAction(u'还原 ', self, triggered=self.child.show)
        self.QuitAction = QAction(u'退出 ', self, triggered=qApp.quit)
        self.IntroAction = QAction(u'产品介绍', self, triggered=self.fun_introduction)
        self.TutoAction = QAction(u'使用指南', self, triggered=self.fun_tutorial)
        self.tray_menu.addAction(self.RestoreAction)
        self.tray_menu.addAction(self.QuitAction)
        self.tray_menu.addAction(self.IntroAction)
        self.tray_menu.addAction(self.TutoAction)
        #子窗口显示点击事件槽函数
        self.start.clicked.connect(self.child.show)

    def fun_show(self):
        self.child.close()
        self.show()

    def fun_introduction(self):
        self.introduction = Ui_Introduction()
        self.introduction.show()

    def fun_tutorial(self):
        self.tutorial = Ui_Tutorial ()
        self.tutorial.show()



