from Color import *

import sys
from  sympy import *


class DlgSetLength5(QtWidgets.QMainWindow):    
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainColor()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Greys)
        self.ui.pushButton_2.clicked.connect(self.Purples)
        self.ui.pushButton_3.clicked.connect(self.Blues)
        self.ui.pushButton_4.clicked.connect(self.Greens)
        self.ui.pushButton_5.clicked.connect(self.Oranges)
        self.ui.pushButton_6.clicked.connect(self.Reds)
        self.ui.pushButton_7.clicked.connect(self.YIOrBr)
        self.ui.pushButton_8.clicked.connect(self.PuRd)
        self.ui.pushButton_9.clicked.connect(self.RdPu)
        self.ui.pushButton_10.clicked.connect(self.BuPu)
        self.ui.pushButton_11.clicked.connect(self.GnBu)
        self.ui.pushButton_12.clicked.connect(self.BuGn)
        self.ui.pushButton_13.clicked.connect(self.YIGn)

    def Greys(self):
        self.parent().color='Greys'
        self.parent().show()
        self.close()
    def Purples(self):
        self.parent().color='Purples'
        self.parent().show()
        self.close()
    def Blues(self):
        self.parent().color='Blues'
        self.parent().show()
        self.close()
    def Greens(self):
        self.parent().color='Greens'
        self.parent().show()
        self.close()
    def Oranges(self):
        self.parent().color='Oranges'
        self.parent().show()
        self.close()
    def Reds(self):
        self.parent().color='Reds'
        self.parent().show()
        self.close()
    def YIOrBr(self):
        self.parent().color='YlOrBr'
        self.parent().show()
        self.close()
    def PuRd(self):
        self.parent().color='PuRd'
        self.parent().show()
        self.close()
    def RdPu(self):
        self.parent().color='RdPu'
        self.parent().show()
        self.close()
    def BuPu(self):
        self.parent().color='BuPu'
        self.parent().show()
        self.close()
    def GnBu(self):
        self.parent().color='GnBu'
        self.parent().show()
        self.close()
    def BuGn(self):
        self.parent().color='BuGn'
        self.parent().show()
        self.close()
    def YIGn(self):
        self.parent().color='YlGn' 
        self.parent().show()
        self.close()
