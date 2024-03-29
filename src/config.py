"""
**********************************************************************************************
config.py

Configuration info (mainly constants) used in covid19.py.

J. Les Gainous
2020-05-16
**********************************************************************************************
"""
from enum import Enum


class ChartFocus(Enum):
    CASES = 1
    NEW_CASES = 2
    DEATHS = 3
    NEW_DEATHS = 4

APP_VERSION: str = "1.00.004"
DATA_URL: str = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
LOCAL_DATA_FILE_NAME: str = r"data\covid19.csv"
LOCAL_STATES_COUNTIES_FILE_NAME: str = r"data\states-counties.csv"
UNUSED_COLUMNS: list = ["county", "state", "fips"]
TICK_REDUCTION_FACTOR: float = 0.98
CHART_FILENAME: str = r".\chart\covid-19-{}-{}-county-{}-{}.png"
ROLLING_AVG_INTERVAL_DAYS: int = 7
