from PyQt5.QtWidgets import *
from AGUI_father import Ui_fatherWindow

class Ui_fatherWindow1(Ui_fatherWindow):
    def __init__(self):
        super(Ui_fatherWindow1, self).__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.close)
        self.exit.clicked.connect(qApp.quit)