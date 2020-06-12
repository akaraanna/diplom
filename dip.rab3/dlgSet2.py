from form_set2 import *

import sys
from  sympy import *


class DlgSetLength2(QtWidgets.QMainWindow):    
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Set_layer()
        self.ui.setupUi(self)
        self.ui.save_set.clicked.connect(self.savepoll)

    def savepoll(self):
        self.parent().update('слой')
        self.parent().show()
        self.close()
