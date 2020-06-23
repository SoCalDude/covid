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
        MainWindow.resize(459, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chkSavePlotImage = QtWidgets.QCheckBox(self.centralwidget)
        self.chkSavePlotImage.setGeometry(QtCore.QRect(40, 262, 125, 20))
        self.chkSavePlotImage.setChecked(True)
        self.chkSavePlotImage.setObjectName("chkSavePlotImage")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(-1, 10, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(270, 300, 75, 24))
        self.btnStart.setObjectName("btnStart")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(350, 300, 75, 24))
        self.btnClose.setObjectName("btnClose")
        self.grpDataSource = QtWidgets.QGroupBox(self.centralwidget)
        self.grpDataSource.setGeometry(QtCore.QRect(250, 162, 181, 81))
        self.grpDataSource.setObjectName("grpDataSource")
        self.radServerData = QtWidgets.QRadioButton(self.grpDataSource)
        self.radServerData.setGeometry(QtCore.QRect(20, 20, 151, 20))
        self.radServerData.setChecked(True)
        self.radServerData.setObjectName("radServerData")
        self.radLocalData = QtWidgets.QRadioButton(self.grpDataSource)
        self.radLocalData.setGeometry(QtCore.QRect(20, 50, 151, 20))
        self.radLocalData.setObjectName("radLocalData")
        self.grpMetric = QtWidgets.QGroupBox(self.centralwidget)
        self.grpMetric.setGeometry(QtCore.QRect(30, 162, 181, 81))
        self.grpMetric.setObjectName("grpMetric")
        self.radNewCases = QtWidgets.QRadioButton(self.grpMetric)
        self.radNewCases.setGeometry(QtCore.QRect(20, 20, 151, 20))
        self.radNewCases.setChecked(True)
        self.radNewCases.setObjectName("radNewCases")
        self.radNewDeaths = QtWidgets.QRadioButton(self.grpMetric)
        self.radNewDeaths.setGeometry(QtCore.QRect(20, 50, 151, 20))
        self.radNewDeaths.setObjectName("radNewDeaths")
        self.lblVersion = QtWidgets.QLabel(self.centralwidget)
        self.lblVersion.setGeometry(QtCore.QRect(20, 310, 211, 10))
        self.lblVersion.setObjectName("lblVersion")
        self.grpLocation = QtWidgets.QGroupBox(self.centralwidget)
        self.grpLocation.setGeometry(QtCore.QRect(30, 60, 401, 81))
        self.grpLocation.setObjectName("grpLocation")
        self.lblState = QtWidgets.QLabel(self.grpLocation)
        self.lblState.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.lblState.setObjectName("lblState")
        self.cboStates = QtWidgets.QComboBox(self.grpLocation)
        self.cboStates.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.cboStates.setCurrentText("")
        self.cboStates.setObjectName("cboStates")
        self.lblCounty = QtWidgets.QLabel(self.grpLocation)
        self.lblCounty.setGeometry(QtCore.QRect(220, 20, 47, 13))
        self.lblCounty.setObjectName("lblCounty")
        self.cboCounties = QtWidgets.QComboBox(self.grpLocation)
        self.cboCounties.setGeometry(QtCore.QRect(220, 40, 161, 20))
        self.cboCounties.setObjectName("cboCounties")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orange Co. COVID-19 Charting"))
        self.chkSavePlotImage.setText(_translate("MainWindow", "Save chart image"))
        self.lblTitle.setText(_translate("MainWindow", "County COVID-19 Charting"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
        self.grpDataSource.setTitle(_translate("MainWindow", "Data Source"))
        self.radServerData.setText(_translate("MainWindow", "via Internet"))
        self.radLocalData.setText(_translate("MainWindow", "via local previous data"))
        self.grpMetric.setTitle(_translate("MainWindow", "Chart Data"))
        self.radNewCases.setText(_translate("MainWindow", "Daily new cases"))
        self.radNewDeaths.setText(_translate("MainWindow", "Daily new deaths"))
        self.lblVersion.setText(_translate("MainWindow", "v0.10"))
        self.grpLocation.setTitle(_translate("MainWindow", "Location"))
        self.lblState.setText(_translate("MainWindow", "State:"))
        self.lblCounty.setText(_translate("MainWindow", "County:"))
