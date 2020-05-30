# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Анна\Desktop\dip.rab2\form_set2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Set_layer(object):
    def setupUi(self, Set_layer):
        Set_layer.setObjectName("Set_layer")
        Set_layer.resize(289, 241)
        font = QtGui.QFont()
        font.setPointSize(8)
        Set_layer.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("science.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Set_layer.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Set_layer)
        self.centralwidget.setObjectName("centralwidget")
        self.set_x = QtWidgets.QTextEdit(self.centralwidget)
        self.set_x.setGeometry(QtCore.QRect(60, 10, 211, 31))
        self.set_x.setObjectName("set_x")
        self.save_set = QtWidgets.QPushButton(self.centralwidget)
        self.save_set.setGeometry(QtCore.QRect(60, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_set.setFont(font)
        self.save_set.setObjectName("save_set")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.set_y = QtWidgets.QTextEdit(self.centralwidget)
        self.set_y.setGeometry(QtCore.QRect(60, 50, 211, 31))
        self.set_y.setObjectName("set_y")
        self.set_z = QtWidgets.QTextEdit(self.centralwidget)
        self.set_z.setGeometry(QtCore.QRect(60, 90, 211, 31))
        self.set_z.setObjectName("set_z")
        self.set_z_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.set_z_2.setGeometry(QtCore.QRect(60, 130, 211, 31))
        self.set_z_2.setObjectName("set_z_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        Set_layer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Set_layer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 19))
        self.menubar.setObjectName("menubar")
        Set_layer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Set_layer)
        self.statusbar.setObjectName("statusbar")
        Set_layer.setStatusBar(self.statusbar)

        self.retranslateUi(Set_layer)
        QtCore.QMetaObject.connectSlotsByName(Set_layer)

    def retranslateUi(self, Set_layer):
        _translate = QtCore.QCoreApplication.translate
        Set_layer.setWindowTitle(_translate("Set_layer", "Ввод данных"))
        self.save_set.setText(_translate("Set_layer", "Сохранить"))
        self.label_2.setText(_translate("Set_layer", "по Y"))
        self.label_3.setText(_translate("Set_layer", "по Z"))
        self.label.setText(_translate("Set_layer", "по X"))
        self.label_4.setText(_translate("Set_layer", "Слой"))


