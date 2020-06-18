# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\Les\Documents\python\projects\covid19\gui\mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 195)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chkSavePlotImage = QtWidgets.QCheckBox(self.centralwidget)
        self.chkSavePlotImage.setGeometry(QtCore.QRect(220, 110, 125, 20))
        self.chkSavePlotImage.setChecked(True)
        self.chkSavePlotImage.setObjectName("chkSavePlotImage")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(0, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(200, 160, 75, 24))
        self.btnStart.setObjectName("btnStart")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(280, 160, 75, 24))
        self.btnClose.setObjectName("btnClose")
        self.grpDataSource = QtWidgets.QGroupBox(self.centralwidget)
        self.grpDataSource.setGeometry(QtCore.QRect(20, 60, 181, 81))
        self.grpDataSource.setObjectName("grpDataSource")
        self.radServerData = QtWidgets.QRadioButton(self.grpDataSource)
        self.radServerData.setGeometry(QtCore.QRect(20, 20, 151, 20))
        self.radServerData.setChecked(True)
        self.radServerData.setObjectName("radServerData")
        self.radLocalData = QtWidgets.QRadioButton(self.grpDataSource)
        self.radLocalData.setGeometry(QtCore.QRect(20, 50, 151, 20))
        self.radLocalData.setObjectName("radLocalData")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orange Co. COVID-19 Charting"))
        self.chkSavePlotImage.setText(_translate("MainWindow", "Save plot image"))
        self.lblTitle.setText(_translate("MainWindow", "County COVID-19 Charting"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
        self.grpDataSource.setTitle(_translate("MainWindow", "Data Source"))
        self.radServerData.setText(_translate("MainWindow", "via Internet"))
        self.radLocalData.setText(_translate("MainWindow", "via local previous data"))
