from PyQt5 import QtCore, QtGui, QtWidgets

def SetWindowPreferences(targetWindow: QtWidgets.QMainWindow) -> None:
    targetWindow.setFixedSize(374, 195)

    return