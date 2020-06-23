import sys
from  sympy import *
import forma as fm
from PyQt5 import QtCore, QtGui, QtWidgets
import dlgSet1  as dlgS1
import dlgSet3  as dlgS3
import dlgSet5  as dlgS5
import fun as function
import  xlwt
import numpy as np
import traceback
from PyQt5.QtCore import QThread, pyqtSignal
import time

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


class MyWin(QtWidgets.QMainWindow):    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = fm.Ui_MainWindow()
        self.ui.setupUi(self)
        #активность некоторых кнопок отключаем
        self.ui.set_poll.setEnabled(False)
        self.ui.start.setEnabled(False)
        self.ui.reset.setEnabled(False)
        self.ui.excel.setEnabled(False)
        self.nx=40
        self.ny=40
        self.nz=40
        self.mx=10
        self.my=10
        self.mz=10
        self.iter=0
        self.px=0
        self.py=0
        self.pz=0
        self.polls=''
        self.biass=''
        self.color='PuRd'
        self.formyl=''
        #выводимые поля формы
        self.ui.grid.textChanged.connect(self.KeyPressEvent)
        self.ui.poll.textChanged.connect(self.KeyPressEvent)
        self.ui.bias.textChanged.connect(self.KeyPressEvent)
        self.ui.layer.textChanged.connect(self.KeyPressEvent)
        self.ui.textEdit_5.textChanged.connect(self.KeyPressEvent)
        self.ui.checkBox_2.stateChanged.connect(self.KeyPressEvent)
        #определяем какое событие будет происходить при наж на кнопку
        self.ui.set_grid.clicked.connect(self.basisModalDialog)
        self.ui.set_poll.clicked.connect(self.basisModalDialog3)
        self.ui.set_color.clicked.connect(self.basisModalDialog5)
        self.ui.start.clicked.connect(self.starter)
        self.ui.reset.clicked.connect(self.reseter)
        self.ui.excel.clicked.connect(self.excel)
    
 
    def KeyPressEvent(self):
        if(self.ui.grid.toPlainText() and self.ui.poll.toPlainText() and self.ui.bias.toPlainText()
           and (self.ui.layer.toPlainText() or self.ui.checkBox_2.isChecked() == True) and self.ui.textEdit_5.toPlainText()):
            self.ui.start.setEnabled(True)
        else: self.ui.start.setEnabled(False)
        if(self.ui.grid.toPlainText() or self.ui.poll.toPlainText()):
            self.ui.reset.setEnabled(True)
        else: self.ui.reset.setEnabled(False)
        if self.ui.checkBox_2.isChecked() == True :
            self.ui.layer.setEnabled(False)
        else :
            self.ui.layer.setEnabled(True)

    def starter(self):
        self.ui.set_grid.setEnabled(False)
        self.chet=int(self.ui.textEdit_5.toPlainText())
        
        self.ui.start.setEnabled(False)
        self.ui.reset.setEnabled(False)
        self.ui.excel.setEnabled(False)
        self.ui.set_poll.setEnabled(False)
        self.ui.set_color.setEnabled(False)

        if(self.ui.checkBox_2.isChecked() == True):
            if(self.ui.checkBox.isChecked() == True):
                self.thread = podschetWithAnimation_3D(self.Uold,self.iter,self.chet,self.nx,self.ny,self.nz)
                self.thread.finished.connect(self.on_finishedWithAnimation_3D)
            else:
                self.thread = podschet(self.Uold,self.iter,self.chet)
                self.thread.finished.connect(self.on_finished_3D)
        else:
            self.slo=int(self.ui.layer.toPlainText())
            if(self.ui.checkBox.isChecked() == True):
                self.thread = podschetWithAnimation(self.Uold,self.iter,self.chet,self.ui.radioButton_3.isChecked(),self.ui.radioButton_2.isChecked(),self.slo,self.nx,self.ny,self.nz)
                self.thread.finished.connect(self.on_finishedWithAnimation)
            else:
                self.thread = podschet(self.Uold,self.iter,self.chet)
                self.thread.finished.connect(self.on_finished)
                
        self.thread.progressed.connect(self.on_progress)
        self.thread.start()
        

    def on_progress(self, value):
        self.ui.textEdit_6.setText(str(value))
    
    def on_finished(self):
        self.iter += self.chet
        self.Uold = self.thread.Uold
        self.ui.start.setEnabled(True)
        self.ui.reset.setEnabled(True)
        self.ui.excel.setEnabled(True)
        self.ui.set_poll.setEnabled(True)
        self.ui.set_color.setEnabled(True)
        if self.ui.radioButton_3.isChecked() == True :
            print('z')
            self.graffz()
        elif self.ui.radioButton_2.isChecked() == True :
            print('y')
            self.graffy()
        else :
           print('x')
           self.graffx()

    def on_finishedWithAnimation(self):
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        ims=[]
        co=plt.get_cmap(self.color)
        try:
            for i in range(self.chet + 1):
                z = self.thread.visArrayZ[i]
                x = self.thread.visArrayX[i]
                y = self.thread.visArrayY[i]
                
                sf = ax.plot_trisurf(x, y, z, cmap=co,vmin=0., vmax=1., linewidth=0, antialiased=False)
                ims.append([sf])

            ax.set_title(str(self.iter) + '-' + str(self.iter + self.chet)  + ' итераций')
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

            ani = animation.ArtistAnimation(fig,ims,interval = 10, blit = False)
            plt.show()



        except Exception as e:
           print('Ошибка:\n', traceback.format_exc())

        self.iter += self.chet
        self.Uold = self.thread.Uold
        self.ui.start.setEnabled(True)
        self.ui.reset.setEnabled(True)
        self.ui.excel.setEnabled(True)
        self.ui.set_poll.setEnabled(True)

    def on_finished_3D(self):
        self.iter += self.chet
        self.Uold = self.thread.Uold
        self.ui.start.setEnabled(True)
        self.ui.reset.setEnabled(True)
        self.ui.excel.setEnabled(True)
        self.ui.set_poll.setEnabled(True)
        self.ui.set_color.setEnabled(True)
        self.graff_3D()


    def on_finishedWithAnimation_3D(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        co=plt.get_cmap(self.color)
        ims=[]
        try:
            for i in range(self.chet + 1):
                al = self.thread.visArrayAL[i]
                z = self.thread.visArrayZ[i]
                x = self.thread.visArrayX[i]
                y = self.thread.visArrayY[i]
                
                sf = ax.scatter(x, y, z, s=al,c='r')
                ims.append([sf])

            ax.set_title('Распространение на '+str(self.iter) + '-' + str(self.iter + self.chet)  + ' итераций')
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

            ani = animation.ArtistAnimation(fig,ims,interval = 10, blit = False)
            plt.show()



        except Exception as e:
           print('Ошибка:\n', traceback.format_exc())

        self.iter += self.chet
        self.Uold = self.thread.Uold
        self.ui.start.setEnabled(True)
        self.ui.reset.setEnabled(True)
        self.ui.excel.setEnabled(True)
        self.ui.set_poll.setEnabled(True)
    
    def pollution(self,xs,xe,ys,ye,zs,ze):
        try:
           self.Uold[1][1][1]
        except:
           self.Uold=[[[0 for _ in range(self.nz)] for _ in range(self.ny)] for _ in range(self.nx)]
 
        for i in range(xs,xe):
            for j in range(ys,ye):
                for k in range(zs,ze):
                    self.Uold[i][j][k]=1

                    
    def pollFormyl(self,xs,xe,ys,ye,zs,ze):
        try:
           self.Uold[1][1][1]
        except:
            #если его нет, то создадим
           self.Uold=[[[0 for _ in range(self.nz)] for _ in range(self.ny)] for _ in range(self.nx)]

        expr = sympify(self.formyl)
        for i in range(xs,xe):
            for j in range(ys,ye):
                for k in range(zs,ze):
                   
                    #функ-ия подставляет под х число
                    if expr.subs ([('x',i),('y',j),('z',k)])==0:
                        self.Uold[int(i+self.nx/2+self.px/2)][int(j+self.ny/2+self.py/2)][int(k+self.nz/2+self.pz/2)]=1

    def basisModalDialog(self):
        
        self.dlg = dlgS1.DlgSetLength(self)
        self.hide()
        self.dlg.show()        
       
    def basisModalDialog3(self):
        
        self.dlg = dlgS3.DlgSetLength3(self)
        self.hide()
        self.dlg.show()
   
    def basisModalDialog5(self):
        
        self.dlg = dlgS5.DlgSetLength5(self)
        self.hide()
        self.dlg.show()

    def reseter(self):
        self.ui.set_grid.setEnabled(True)
        self.ui.start.setEnabled(False)
        self.ui.excel.setEnabled(False)
        self.ui.set_poll.setEnabled(False)
        self.iter=0
        self.polls=''
        self.biass=''
	self.formyl=''
        self.ui.poll.setText(self.polls)
        self.ui.bias.setText(self.biass)
        self.ui.grid.setText(' ')
        self.ui.layer.setText(' ')
        self.ui.textEdit_5.setText(' ')
        self.ui.textEdit_6.setText(' ')
        self.Uold = []
        self.ui.reset.setEnabled(False)
       
    def excel(self):
	#необходимо внести корректировки
        wb = xlwt.Workbook()
        ws = wb.add_sheet('diffuzia')
        if (self.ui.radioButton_3.isChecked() == True and self.slo>0) :
            for i in range(self.nx):
                for j in range(self.ny):
                    ws.write(i,j,self.Uold[i][j][self.slo])
            
        elif (self.ui.radioButton_2.isChecked() == True and self.slo>0) :
            for i in range(self.nx):
                for k in range(self.nz):
                    ws.write(i,k,self.Uold[i][self.slo][k])

        else : 
            for k in range(self.nz):
                for j in range(self.ny):
                    ws.write(j,k,self.Uold[self.slo][j][k])
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', '/home/res')[0]
        print(fname)
        wb.save(fname+'.xls')

    def graff_3D(self):
        x,y,z,al = [],[],[],[]
        print('graff_3D')
        for i in range(self.nx):
            for j in range(self.ny):
                for k in range(self.nz):
                    x.append(i)
                    y.append(j)
                    z.append(k) 
                    al.append(self.Uold[i][j][k] if self.Uold[i][j][k] >= 0.0001 else 0) 
        
        self.vis3D(x,y,z,al)       
    
    def vis3D(self,x,y,z,al):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        co=plt.get_cmap(self.color)
        try:
            surf = ax.scatter(x, y, z, s=al,c='r') 
            ax.set_title('Распространение на '+str(self.iter) + ' итерации')

            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

            # Add a color bar which maps values to colors.
            #fig.colorbar(surf, shrink=0.5, aspect=5)

            plt.show()
        except Exception as e:
           print('Ошибка:\n', traceback.format_exc())
           
    def vis(self,x,y,z):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        print('fghjhgf')
        co=plt.get_cmap(self.color)
        try:
            surf = ax.plot_trisurf(x, y, z, cmap=co,vmin=0., vmax=1.,
                       linewidth=0, antialiased=False)

            ax.set_title(str(self.iter) + ' итераций')
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

            # Add a color bar which maps values to colors.
            fig.colorbar(surf, shrink=0.5, aspect=5)

            plt.show()
        except Exception as e:
           print('Ошибка:\n', traceback.format_exc())

    def graffz(self):
        x,y,z=[],[],[]
        for i in range(self.nx):
            for j in range(self.ny):
                x.append(i)
                y.append(j)
                z.append(self.Uold[i][j][self.slo]) 
        self.vis(x,y,z)
        
    def graffy(self):
        x,y,z=[],[],[]
        for i in range(self.nx):
            for k in range(self.nz):
                x.append(i)
                y.append(k)
                z.append(self.Uold[i][self.slo][k])  
        
        self.vis(x,y,z) 

    def graffx(self):
        x,y,z=[],[],[]
        for j in range(self.ny):
            for k in range(self.nz):
                x.append(j)
                y.append(k)
                z.append(self.Uold[self.slo][j][k]) 
        self.vis(x,y,z) 


class podschet(QThread):
    progressed = pyqtSignal(int)

    def __init__(self,Uold,iter,chet):
        super().__init__()
        self.chet = chet
        self.iter = iter
        self.Uold = Uold

    def run(self):        
        for _ in range(self.chet):
            self.Uold=function.raship(self.Uold)
            self.iter=self.iter+1
            self.progressed.emit(self.iter)
            time.sleep(0.5)
        


class podschetWithAnimation(QThread):
    progressed = pyqtSignal(int)

    def __init__(self,Uold,iter,chet,bool1,bool2,slo,nx,ny,nz):
        super().__init__()
        self.chet = chet
        self.iter = iter
        self.Uold = Uold
        self.b1 = bool1
        self.b2 = bool2
        self.slo = slo
        self.nx = nx
        self.ny = ny
        self.nz = nz


    def run(self):
        self.visArrayZ = []
        self.visArrayY = []
        self.visArrayX = []
        for k in range(self.chet):
            if self.b1 == True :
                x,y,z = [],[],[]
                for i in range(self.nx):
                    for j in range(self.ny):
                        x.append(i)
                        y.append(j)
                        z.append(self.Uold[i][j][self.slo])
                self.visArrayX.append(x)
                self.visArrayY.append(y)
                self.visArrayZ.append(z)
            elif self.b2 == True:
                x,y,z = [],[],[]
                for i in range(self.nx):
                    for j in range(self.nz):
                        x.append(i)
                        y.append(j)
                        z.append(self.Uold[i][self.slo][j])
                self.visArrayX.append(x)
                self.visArrayY.append(y)
                self.visArrayZ.append(z)
            else :
                x,y,z = [],[],[]
                for i in range(self.ny):
                    for j in range(self.nz):
                        x.append(i)
                        y.append(j)                        
                        z.append(self.Uold[self.slo][i][j])
                self.visArrayX.append(x)
                self.visArrayY.append(y)
                self.visArrayZ.append(z)

            self.Uold=function.raship(self.Uold)
            self.iter=self.iter+1
            self.progressed.emit(self.iter)
            time.sleep(0.5)

        time.sleep(0.5)
        if self.b1 == True :
            x,y,z = [],[],[]
            for i in range(self.nx):
                for j in range(self.ny):
                    x.append(i)
                    y.append(j)
                    z.append(self.Uold[i][j][self.slo])
            self.visArrayX.append(x)
            self.visArrayY.append(y)
            self.visArrayZ.append(z)
        elif self.b2 == True:
            x,y,z = [],[],[]
            for i in range(self.nx):
                for j in range(self.nz):
                    x.append(i)
                    y.append(j)
                    z.append(self.Uold[i][self.slo][j])
            self.visArrayX.append(x)
            self.visArrayY.append(y)
            self.visArrayZ.append(z)
        else :
            x,y,z = [],[],[]
            for i in range(self.ny):
                for j in range(self.nz):
                    x.append(i)
                    y.append(j)                        
                    z.append(self.Uold[self.slo][i][j])
            self.visArrayX.append(x)
            self.visArrayY.append(y)
            self.visArrayZ.append(z)

class podschetWithAnimation_3D(QThread):
    progressed = pyqtSignal(int)

    def __init__(self,Uold,iter,chet,nx,ny,nz):
        super().__init__()
        self.chet = chet
        self.iter = iter
        self.Uold = Uold
        self.nx = nx
        self.ny = ny
        self.nz = nz

    def run(self):
        self.visArrayAL = []
        self.visArrayZ = []
        self.visArrayY = []
        self.visArrayX = []
        for k in range(self.chet):
            x,y,z,al = [],[],[],[]
            for i in range(self.nx):
                for j in range(self.ny):
                    for k in range(self.nz):
                        x.append(i)
                        y.append(j)
                        z.append(k)
                        al.append(self.Uold[i][j][k] if self.Uold[i][j][k] >= 0.0001 else 0)
            self.visArrayX.append(x)
            self.visArrayY.append(y)
            self.visArrayZ.append(z)
            self.visArrayAL.append(al)

            self.Uold=function.raship(self.Uold)
            self.iter=self.iter+1
            self.progressed.emit(self.iter)
            time.sleep(0.5)

        time.sleep(0.5)
        x,y,z,al = [],[],[],[]
        for i in range(self.nx):
            for j in range(self.ny):
                for k in range(self.nz):
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    al.append(self.Uold[i][j][k] if self.Uold[i][j][k] >= 0.0001 else 0)
        self.visArrayX.append(x)
        self.visArrayY.append(y)
        self.visArrayZ.append(z)
        self.visArrayAL.append(al)

        
app = QtWidgets.QApplication(sys.argv)
myapp = MyWin()
myapp.show()
app.exec_()



    

        
