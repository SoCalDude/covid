"""
**********************************************************************************************
config.py

Configuration info (mainly constants) used in covid19-oc.py.

J. Les Gainous
2020-05-16

Revisions:
Date       Who             Summary
---------- --------------- -------------------------------------------------------------------
yyyy-mm-dd {who}           {short summary}

**********************************************************************************************
"""
from enum import Enum


class ChartFocus(Enum):
    CASES = 1
    NEW_CASES = 2
    DEATHS = 3
    NEW_DEATHS = 4


USE_SERVER_DATA: bool = True
SAVE_CHART_IMAGE: bool = True
DATA_URL: str = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
LOCAL_FILE: str = r"data\covid19.csv"
TARGET_FIPS_ID: float = 6059
UNUSED_COLUMNS: list = ["county", "state", "fips"]
TICK_REDUCTION_FACTOR: float = 0.955
CHART_FILENAME = r".\chart\covid-19-new-cases-{}.png"
