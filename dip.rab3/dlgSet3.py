from form_set3 import *

import sys
from  sympy import *
#from PyQt5 import QtCore, QtGui, QtWidgets

class DlgSetLength3(QtWidgets.QMainWindow):    
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Set_poll()
        self.ui.setupUi(self)
        self.ui.save_set.clicked.connect(self.savelayer)

    def savelayer(self):
        self.ui.save_set.setEnabled(False)
        self.parent().mx=int(self.ui.set_x.toPlainText())
        self.parent().my=int(self.ui.set_y.toPlainText())
        self.parent().mz=int(self.ui.set_z.toPlainText())
        self.parent().px=int(self.ui.set_x_2.toPlainText())
        self.parent().py=int(self.ui.set_y_2.toPlainText())
        self.parent().pz=int(self.ui.set_z_2.toPlainText())
        self.parent().formyl=self.ui.set_Formyl.toPlainText()
        #добавить загрязнение
        if self.ui.set_Formyl.toPlainText():
            t=False
            for i in self.parent().formyl:
                if (i=='x'or i=='y'or i=='z'):
                    t=True        
            if t:
                self.parent().pollFormyl((int)(-self.parent().nx/2-self.parent().px),(int)(self.parent().nx/2-self.parent().px),
                                        (int)(-self.parent().ny/2-self.parent().py),(int)(self.parent().ny/2-self.parent().py),
                                        (int)(-self.parent().nz/2-self.parent().pz),(int)(self.parent().nz/2-self.parent().pz))
                self.parent().ui.poll.setText(self.parent().formyl)
                self.parent().biass=self.parent().biass+str('('+str(self.parent().px)+';'+str(self.parent().py)+';'+str(self.parent().pz)+')    ')
                self.parent().ui.bias.setText(self.parent().biass)
        else :
            self.parent().pollution((int)((self.parent().nx/2)-(self.parent().mx/2)+self.parent().px),(int)((self.parent().nx/2) + (self.parent().mx/2)+self.parent().px),
            (int)((self.parent().ny/ 2) - (self.parent().my/2)+self.parent().py),(int)((self.parent().ny/ 2) + (self.parent().my/2)+self.parent().py),
            (int)((self.parent().nz/ 2) - (self.parent().mz/2)+self.parent().pz), (int)((self.parent().nz/ 2) + (self.parent().mz/2)+self.parent().pz))
            self.parent().polls=self.parent().polls+str('('+str(self.parent().mx)+';'+str(self.parent().my)+';'+str(self.parent().mz)+')    ')
            self.parent().biass=self.parent().biass+str('('+str(self.parent().px)+';'+str(self.parent().py)+';'+str(self.parent().pz)+')    ')
            self.parent().ui.poll.setText(self.parent().polls)
            self.parent().ui.bias.setText(self.parent().biass)
            
        self.ui.save_set.setEnabled(True)
        self.parent().show()
        self.close()
