"""
**********************************************************************************************
utilities.py

Various generic utility functions.

J. Les Gainous
2020-06-18
**********************************************************************************************
"""
def processLogMessage(level: int, message: str, loggers: list) -> None:
    for logger in loggers:
        logger.log(level, message)
