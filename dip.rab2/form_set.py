# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Анна\Desktop\dip.rab2\form_set.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Set_grid(object):
    def setupUi(self, Set_grid):
        Set_grid.setObjectName("Set_grid")
        Set_grid.resize(280, 194)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("science.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Set_grid.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Set_grid)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.set_x = QtWidgets.QTextEdit(self.centralwidget)
        self.set_x.setGeometry(QtCore.QRect(60, 10, 211, 31))
        self.set_x.setObjectName("set_x")
        self.set_y = QtWidgets.QTextEdit(self.centralwidget)
        self.set_y.setGeometry(QtCore.QRect(60, 50, 211, 31))
        self.set_y.setObjectName("set_y")
        self.set_z = QtWidgets.QTextEdit(self.centralwidget)
        self.set_z.setGeometry(QtCore.QRect(60, 90, 211, 31))
        self.set_z.setObjectName("set_z")
        self.save_set = QtWidgets.QPushButton(self.centralwidget)
        self.save_set.setGeometry(QtCore.QRect(60, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_set.setFont(font)
        self.save_set.setObjectName("save_set")
        Set_grid.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Set_grid)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName("menubar")
        Set_grid.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Set_grid)
        self.statusbar.setObjectName("statusbar")
        Set_grid.setStatusBar(self.statusbar)

        self.retranslateUi(Set_grid)
        QtCore.QMetaObject.connectSlotsByName(Set_grid)

    def retranslateUi(self, Set_grid):
        _translate = QtCore.QCoreApplication.translate
        Set_grid.setWindowTitle(_translate("Set_grid", "Ввод данных"))
        self.label.setText(_translate("Set_grid", "по X"))
        self.label_2.setText(_translate("Set_grid", "по Y"))
        self.label_3.setText(_translate("Set_grid", "по Z"))
        self.set_x.setHtml(_translate("Set_grid", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">40</p></body></html>"))
        self.set_y.setHtml(_translate("Set_grid", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">40</p></body></html>"))
        self.set_z.setHtml(_translate("Set_grid", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">40</p></body></html>"))
        self.save_set.setText(_translate("Set_grid", "Сохранить"))


