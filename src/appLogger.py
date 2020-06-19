"""
**********************************************************************************************
appLogger.py

Class file for application logging.

J. Les Gainous
2020-06-18
**********************************************************************************************
"""
import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler


class AppLogger:
    def __init__(
        self,
        name: str = "myLogger",
        level: str = "debug",
        target: str = "console",
        filename: str = "",
        format: str = "",
    ):
        self.name = name
        self.level = level.lower()
        self.target = target.lower()
        self.filename = filename
        if format == "":
            # default format
            self.formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s:%(funcName)s|%(message)s")
        else:
            self.formatter = logging.Formatter(format)

    def makeLogger(self) -> logging.Logger:
        logger = logging.getLogger(self.name)

        # Python's default logger level is Warning, if no level requested
        if self.level == "debug":
            logger.setLevel(logging.DEBUG)
        elif self.level == "info":
            logger.setLevel(logging.INFO)
        elif self.level == "warning":
            logger.setLevel(logging.WARNING)
        elif self.level == "error":
            logger.setLevel(logging.ERROR)
        elif self.level == "critical":
            logger.setLevel(logging.CRITICAL)

        if self.target == "console":
            logHandler = logging.StreamHandler()
            logHandler.setFormatter(self.formatter)
        elif self.target == "onefile":
            self.__prepForFile(self.filename)
            logHandler = logging.FileHandler(self.filename, mode="a")
            logHandler.setFormatter(self.formatter)
        elif self.target == "dailyfile":
            # treated as a TimedRotatingFileHandler on a daily rotation
            self.__prepForFile(self.filename)
            logHandler = TimedRotatingFileHandler(self.filename, when="midnight", interval=1, backupCount=14, utc=True)
            logHandler.setFormatter(self.formatter)
        elif self.target == "consoleAndFile":
            logger.addHandler(logging.FileHandler(self.filename, mode="a"))
            logger.addHandler(logging.StreamHandler())
            logHandler.setFormatter(self.formatter)
        else:
            logHandler = logging.StreamHandler()
            logHandler.setFormatter(self.formatter)

        logging.Formatter.converter = time.gmtime  # express time in UTC
        if self.target != "consoleAndFile":
            logger.addHandler(logHandler)

        return logger

    def __makeLoggerObsolete(self) -> logging.Logger:
        """ This is not a ready for primetime. It is still a work-in-progress. The goal of this is to have 
        one logger that outputs to two targets (console and file). It works, as long as I give the logger 
        a name, otherwise, it logs everything, including third-party packages/modules. <not good!> """
        root = logging.getLogger()

        # Create handler for logging
        if self.target == "console":
            logHandler = logging.StreamHandler()
            logHandler.setFormatter(self.formatter)
        elif self.target == "onefile":
            self.__prepForFile(self.filename)
            logHandler = logging.FileHandler(self.filename, mode="a")
            logHandler.setFormatter(self.formatter)
        elif self.target == "dailyfile":
            # treated as a TimedRotatingFileHandler on a daily rotation
            self.__prepForFile(self.filename)
            logHandler = TimedRotatingFileHandler(self.filename, when="midnight", interval=1, backupCount=14)
            logHandler.setFormatter(self.formatter)
        else:
            logHandler = logging.StreamHandler()
            logHandler.setFormatter(self.formatter)

        # Python's default logger level is Warning, if no level requested
        if self.level == "debug":
            root.setLevel(logging.DEBUG)
            logHandler.setLevel(logging.DEBUG)
        elif self.level == "info":
            root.setLevel(logging.INFO)
            logHandler.setLevel(logging.INFO)
        elif self.level == "warning":
            root.setLevel(logging.WARNING)
            logHandler.setLevel(logging.WARNING)
        elif self.level == "error":
            root.setLevel(logging.ERROR)
            logHandler.setLevel(logging.ERROR)
        elif self.level == "critical":
            root.setLevel(logging.CRITICAL)
            logHandler.setLevel(logging.CRITICAL)

        logging.Formatter.converter = time.gmtime  # express time in UTC

        root.addHandler(logHandler)

        return root

    def __prepForFile(self, fullPath: str) -> None:
        if len(fullPath.strip()) > 0:
            if not (os.path.exists(os.path.dirname(fullPath))):
                os.makedirs(os.path.dirname(fullPath))

