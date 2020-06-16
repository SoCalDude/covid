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
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(200, 160, 75, 24))
        self.btnOK.setObjectName("btnOK")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(280, 160, 75, 24))
        self.btnCancel.setObjectName("btnCancel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 181, 81))
        self.groupBox.setObjectName("groupBox")
        self.radServer = QtWidgets.QRadioButton(self.groupBox)
        self.radServer.setGeometry(QtCore.QRect(20, 20, 151, 20))
        self.radServer.setChecked(True)
        self.radServer.setObjectName("radServer")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 151, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orange Co. COVID-19 Charting"))
        self.chkSavePlotImage.setText(_translate("MainWindow", "Save plot image"))
        self.lblTitle.setText(_translate("MainWindow", "County COVID-19 Charting"))
        self.btnOK.setText(_translate("MainWindow", "OK"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.groupBox.setTitle(_translate("MainWindow", "Data Source"))
        self.radServer.setText(_translate("MainWindow", "via Internet"))
        self.radioButton_2.setText(_translate("MainWindow", "via local previous data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
