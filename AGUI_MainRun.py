from AGUI_mainform import MainForm
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #启动界面
    splash = QSplashScreen(QPixmap("紫霞仙子.jpeg"))
    splash.showMessage("正在加载资源...", Qt.AlignCenter, Qt.red)
    splash.show()
    win = MainForm()
    win.show()
    splash.finish(win)
    sys.exit(app.exec_())