"""
**********************************************************************************************
utilities.py

Various generic utility functions.

J. Les Gainous
2020-06-18
**********************************************************************************************
"""
from PyQt5 import QtCore, QtGui, QtWidgets

def processLogMessage(level: int, message: str, loggers: list) -> None:
    for logger in loggers:
        logger.log(level, message)


def populateComboBox(cbo: QtWidgets.QComboBox, sourceData: list) -> None:
    cbo.addItems(sourceData)



