
from form_set import *
import sys
from  sympy import *


class DlgSetLength(QtWidgets.QMainWindow):    
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Set_grid()
        self.ui.setupUi(self)
        self.ui.save_set.clicked.connect(self.savegrid)

    def savegrid(self):

        self.parent().nx=int(self.ui.set_x.toPlainText())
        self.parent().ny=int(self.ui.set_y.toPlainText())
        self.parent().nz=int(self.ui.set_z.toPlainText())
        self.parent().ui.grid.setText(str('('+str(self.parent().nx)+';'+str(self.parent().ny)+';'+str(self.parent().nz)+')'))
        
        self.parent().ui.set_poll.setEnabled(True)
        self.parent().ui.set_grid.setEnabled(False)
        self.parent().show()
        self.close()
    

    


