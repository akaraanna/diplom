# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Анна\Desktop\dip.rab2\form_set3.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Set_poll(object):
    def setupUi(self, Set_poll):
        Set_poll.setObjectName("Set_poll")
        Set_poll.resize(411, 325)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("science.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Set_poll.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Set_poll)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.set_x = QtWidgets.QTextEdit(self.centralwidget)
        self.set_x.setGeometry(QtCore.QRect(180, 10, 211, 31))
        self.set_x.setObjectName("set_x")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 50, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.set_y = QtWidgets.QTextEdit(self.centralwidget)
        self.set_y.setGeometry(QtCore.QRect(180, 50, 211, 31))
        self.set_y.setObjectName("set_y")
        self.set_z = QtWidgets.QTextEdit(self.centralwidget)
        self.set_z.setGeometry(QtCore.QRect(180, 90, 211, 31))
        self.set_z.setObjectName("set_z")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.set_y_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.set_y_2.setGeometry(QtCore.QRect(180, 180, 211, 31))
        self.set_y_2.setObjectName("set_y_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 220, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.set_x_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.set_x_2.setGeometry(QtCore.QRect(180, 140, 211, 31))
        self.set_x_2.setObjectName("set_x_2")
        self.set_z_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.set_z_2.setGeometry(QtCore.QRect(180, 220, 211, 31))
        self.set_z_2.setObjectName("set_z_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 180, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 140, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.save_set = QtWidgets.QPushButton(self.centralwidget)
        self.save_set.setGeometry(QtCore.QRect(120, 260, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_set.setFont(font)
        self.save_set.setObjectName("save_set")
        Set_poll.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Set_poll)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        Set_poll.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Set_poll)
        self.statusbar.setObjectName("statusbar")
        Set_poll.setStatusBar(self.statusbar)

        self.retranslateUi(Set_poll)
        QtCore.QMetaObject.connectSlotsByName(Set_poll)

    def retranslateUi(self, Set_poll):
        _translate = QtCore.QCoreApplication.translate
        Set_poll.setWindowTitle(_translate("Set_poll", "Ввод данных"))
        self.label_2.setText(_translate("Set_poll", "Размерность \n"
" загрязнения"))
        self.set_x.setHtml(_translate("Set_poll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.label_3.setText(_translate("Set_poll", "по Y"))
        self.label_4.setText(_translate("Set_poll", "по Z"))
        self.label.setText(_translate("Set_poll", "по X"))
        self.set_y.setHtml(_translate("Set_poll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.set_z.setHtml(_translate("Set_poll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.label_5.setText(_translate("Set_poll", "Смещение \n"
" относительно \n"
" центра"))
        self.set_y_2.setHtml(_translate("Set_poll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_6.setText(_translate("Set_poll", "по Z"))
        self.set_x_2.setHtml(_translate("Set_poll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.set_z_2.setHtml(_translate("Set_poll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_7.setText(_translate("Set_poll", "по Y"))
        self.label_8.setText(_translate("Set_poll", "по X"))
        self.save_set.setText(_translate("Set_poll", "Сохранить"))


