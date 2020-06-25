"""
**********************************************************************************************
convid19.py

Main script that kicks off the covid-19 charting app by county.

J. Les Gainous
2020-05-16
**********************************************************************************************
"""
# region Imports
import datetime
import os.path
import shutil
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import sys
import traceback

sys.path.append(".")
import src.config as cfg
import src.utilities as utl

from src.appLogger import AppLogger
from PyQt5 import QtCore, QtGui, QtWidgets, uic

# import mainFormConfig as formCfg
from src.mainForm import Ui_MainWindow

# endregion

# region setup the two loggers (one for console and one for rotating file)
_log1 = AppLogger("consoleLogger", "debug", "console", format="%(message)s")
loggerCon = _log1.makeLogger()

_log1 = AppLogger("rotatingFileLogger", "debug", "dailyFile", r"logs\covid.log")
loggerFile = _log1.makeLogger()

loggers = [loggerCon, loggerFile]
# endregion


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # class-level variable(s)
    _dfStCo: pd.DataFrame = pd.DataFrame()

    # ctor
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # custom event handling (assigning slots)
        self.cboStates.currentIndexChanged.connect(self.loadCountyData)  # state changed, so update the list of counties
        self.btnStart.clicked.connect(self.handleStartButton)
        self.btnClose.clicked.connect(self.handleCloseButton)

        # custom property settings
        self.setWindowIcon(QtGui.QIcon(r"images/covid-image-120x123.png"))
        _translate = QtCore.QCoreApplication.translate
        self.lblVersion.setText(_translate("MainWindow", f"v{cfg.APP_VERSION}"))
        self.setFixedSize(459, 334)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        # load the states and their counties in a class-level dataframe
        MainWindow._dfStCo = self.loadStateCountyData(cfg.LOCAL_DATA_FILE_NAME)

        # initialize the states combobox (dropdown listbox)
        dfSt: pd.DataFrame = MainWindow._dfStCo.groupby(["state"]).size().reset_index()["state"]
        self.cboStates.addItems(dfSt)

    def loadStateCountyData(self, localDataFile: str) -> pd.DataFrame:
        pdRetVal: pd.DataFrame = pd.DataFrame()
        try:
            if os.path.exists(cfg.LOCAL_DATA_FILE_NAME):
                pdRetVal = self.__loadLookupFromPreviousData(cfg.LOCAL_DATA_FILE_NAME)
            else:
                pdRetVal = self.__loadLookupFromStaticFile(cfg.LOCAL_STATES_COUNTIES_FILE_NAME)
        except OSError as oserr:
            utl.processLogMessage(
                logging.ERROR, f"Unable to load lookup data: '{oserr}'", loggers,
            )

        return pdRetVal

    def __loadLookupFromPreviousData(self, localPreviousDataFile: str) -> pd.DataFrame:
        dfStCo: pd.DataFrame = pd.DataFrame()
        try:
            pdAll = pd.read_csv(localPreviousDataFile, delimiter=None, encoding="mbcs")
            dfStCo = pdAll[["state", "county"]]
        except Exception as ex:
            utl.processLogMessage(
                logging.ERROR, f"Unable to read local previous data, '{localPreviousDataFile}'. {ex.__doc__}", loggers,
            )
            raise OSError(f"Unable to read local previous data, '{localPreviousDataFile}'. {ex.__doc__}")
        else:
            dfStCo = self.__loadLookupFromStaticFile(cfg.LOCAL_STATES_COUNTIES_FILE_NAME)

        return dfStCo

    def __loadLookupFromStaticFile(self, localStaticDataFile: str) -> pd.DataFrame:
        dfStCo: pd.DataFrame = pd.DataFrame()
        try:
            dfStCo = pd.read_csv(cfg.LOCAL_DATA_FILE_NAME, delimiter=None, encoding="mbcs")
        except Exception as ex:
            utl.processLogMessage(
                logging.ERROR, f"Unable to read local static data, '{cfg.LOCAL_DATA_FILE_NAME}'. {ex.__doc__}", loggers,
            )
            raise OSError(f"Unable to read local static data, '{cfg.LOCAL_DATA_FILE_NAME}'. {ex.__doc__}")

        return dfStCo

    def loadCountyData(self) -> None:
        dfCo: pd.DataFrame = pd.DataFrame()
        dfCo = MainWindow._dfStCo.groupby(["state", "county"]).size().reset_index()
        dfCo = dfCo[dfCo["state"] == self.cboStates.currentText()]["county"]
        self.cboCounties.clear()
        self.cboCounties.addItems(dfCo)

    def handleStartButton(self) -> None:
        self.btnStart.setEnabled(False)
        self.btnClose.setEnabled(False)
        self.cboStates.setEnabled(False)
        self.cboCounties.setEnabled(False)
        self.grpDataSource.setEnabled(False)
        self.grpMetric.setEnabled(False)
        self.chkSavePlotImage.setEnabled(False)

        chartFocus: cfg.ChartFocus = cfg.ChartFocus.NEW_CASES
        try:
            if self.radNewCases.isChecked():
                chartFocus = cfg.ChartFocus.NEW_CASES
            elif self.radNewDeaths.isChecked():
                chartFocus = cfg.ChartFocus.NEW_DEATHS

            launchOptions = {
                "chartFocus": chartFocus,
                "isFromServer": self.radServerData.isChecked(),
                "saveChart": self.chkSavePlotImage.isChecked(),
                "state": self.cboStates.currentText(),
                "county": self.cboCounties.currentText(),
            }
            launchCharting(launchOptions)
        except:
            errMsg = f"An error occurred: {sys.exc_info()[0]}; {sys.exc_info()[1] if len(sys.exc_info()) > 1 else ''}\n{traceback.format_exc()}"
            utl.processLogMessage(logging.ERROR, errMsg, loggers)
        finally:
            self.btnStart.setEnabled(True)
            self.btnClose.setEnabled(True)
            self.cboStates.setEnabled(True)
            self.cboCounties.setEnabled(True)
            self.grpDataSource.setEnabled(True)
            self.grpMetric.setEnabled(True)
            self.chkSavePlotImage.setEnabled(True)

    def handleCloseButton(self):
        self.close()


class Covid19:
    # ctor
    def __init__(self):
        pass

    def getLatestData(self, fromServer: bool) -> bool:
        retVal: bool = True
        wasRemoteCallSuccessful: bool = True

        if fromServer:
            # make a call to get the latest CSV file
            try:
                csv = requests.get(url=cfg.DATA_URL)
                if (csv.status_code != 200) or (len(csv.text) < 1000):
                    wasRemoteCallSuccessful = False
                    utl.processLogMessage(
                        logging.WARNING,
                        f"Unable to retrieve data from server. HTTP status code: {csv.status_code}. Using local data, if possible.",
                        loggers,
                    )
            except Exception as ex:
                utl.processLogMessage(
                    logging.ERROR,
                    f"The following error occurred. '{ex.__doc__}'. Using local data, if possible.",
                    loggers,
                )
                retVal = False

            # when the call succeeds and there is some text then
            # make a copy of the old file and create the new one
            if retVal and wasRemoteCallSuccessful:
                try:
                    with open(cfg.LOCAL_DATA_FILE_NAME, "w") as f:
                        f.write(csv.text)
                except Exception as ex:
                    utl.processLogMessage(
                        logging.ERROR, f"The following error occurred. '{ex.__doc__}'", loggers,
                    )
                    retVal = False

        return retVal

    def getFilteredData(self, whichState: str, whichCounty: str) -> pd.DataFrame:
        dfFiltered: pd.DataFrame = None

        try:
            df = pd.read_csv(cfg.LOCAL_DATA_FILE_NAME, delimiter=None, encoding="mbcs")
        except Exception as ex:
            utl.processLogMessage(
                logging.ERROR, f"Unable to read local data, '{cfg.LOCAL_DATA_FILE_NAME}'. {ex.__doc__}", loggers,
            )
        else:
            # filter just for the requested fips value. When the dataframe was created,
            # fips was imported as a float64
            dfFiltered = df[df.apply(lambda f: f["state"] == whichState and f["county"] == whichCounty, axis=1)]
            dfFiltered = dfFiltered.drop(cfg.UNUSED_COLUMNS, axis=1)

        return dfFiltered

    def addComputedColumns(self, df: pd.DataFrame) -> None:
        df["NewCases"] = df.cases - df.cases.shift()
        df["NewDeaths"] = df.deaths - df.deaths.shift()
        # shift() causes a NaN in the first row value, so let's change it to the starting value of its corresponding column
        # df.NewCases.iloc[0] = df.cases.iloc[0]  # this produces the SettingWithCopyWarning notice
        # df.NewDeaths.iloc[0] = df.deaths.iloc[0]  # this produces the SettingWithCopyWarning notice
        df.loc[df.index[0], "NewCases"] = df.loc[df.index[0], "cases"]
        df.loc[df.index[0], "NewDeaths"] = df.loc[df.index[0], "deaths"]

        # Rolling average
        df["SMAc"] = df["NewCases"].rolling(14).mean()
        df["SMAd"] = df["NewDeaths"].rolling(14).mean()
        return

    def reduceTicks(self, tickCount: int, percentReduction: float) -> int:
        retVal: int = 0
        if tickCount > 1 and percentReduction > 0:
            retVal = int(round(tickCount * (1 - percentReduction), 0))

        utl.processLogMessage(
            logging.INFO,
            f"Using {tickCount} with a {percentReduction} reduction, reduceTicks() returned {retVal}",
            loggers,
        )

        return retVal

    # converts a string representation of a date to a specifically formatted string date for the graph title
    def getTitleDate(self, dateString: str) -> str:
        stringDate: str = ""
        try:
            stringDate = format(datetime.datetime.strptime(dateString, "%Y-%m-%d").strftime("%B %d, %Y"))
        except ValueError:
            stringDate = ""

        return stringDate

    def getFilenameTimestamp(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d-%H%M")

    def showChart(self, df: pd.DataFrame, whichMetric: cfg.ChartFocus, whichCounty: str, whichState: str, saveChart: bool) -> None:
        yAxis: str = ""
        yLabel: str = ""
        filename_desc: str = ""

        df = df.set_index("date")

        if whichMetric == cfg.ChartFocus.NEW_CASES:
            yAxis = "NewCases"
            yLabel = "New Cases per Day"
            filename_desc = "new-cases"
        elif whichMetric == cfg.ChartFocus.NEW_DEATHS:
            yAxis = "NewDeaths"
            yLabel = "Deaths per Day"
            filename_desc = "new-deaths"

        plt.figure(figsize=(10, 6), dpi=120)
        # Add main data to the graph
        plt.plot(df[yAxis], label=yLabel)
        # Add the moving average to the graph
        plt.plot(
            (df.SMAc if whichMetric == cfg.ChartFocus.NEW_CASES else df.SMAd), label="14-Day Moving Avg",
        )

        # show every x ticks
        plt.xticks(np.arange(0, len(df.index), self.reduceTicks(len(df.index), cfg.TICK_REDUCTION_FACTOR),))

        # set the graph's other appearance properties
        plt.title(
            "Covid-19\n{} County, {}\n(from {} to {}, inclusive)".format(
                whichCounty, whichState, self.getTitleDate(df.index[0]), self.getTitleDate(df.index[len(df.index) - 1]),
            )
        )
        plt.xticks(fontsize=7, rotation=45, ha="right")
        plt.grid(axis="x", which="major", color="#E5E5E5", linestyle="dotted")
        plt.grid(axis="y", which="major", color="#E5E5E5", linestyle="solid")
        plt.legend()

        # if saving the chart is requested
        if saveChart:
            plt.savefig(
                cfg.CHART_FILENAME.format(filename_desc, self.getFilenameTimestamp()), bbox_inches="tight",
            )

        # display chart
        plt.show()


def launchCharting(chartingOptions: dict) -> None:
    cvd = Covid19()
    useServerData = chartingOptions["isFromServer"]

    utl.processLogMessage(logging.INFO, f"Selected data for {chartingOptions['county']} County, {chartingOptions['state']}: {cfg.ChartFocus(chartingOptions['chartFocus']).name}", loggers)

    # this was chosen by the user in the GUI if they want fresh data or not
    utl.processLogMessage(
        logging.INFO, "Retrieving data from server..." if useServerData else "Retrieving from local file...", loggers
    )

    if (not cvd.getLatestData(useServerData)) and (not os.path.isfile(cfg.LOCAL_DATA_FILE_NAME)):
        utl.processLogMessage(
            logging.CRITICAL, "Unable to download latest data nor able to use local data.", loggers,
        )
    else:
        utl.processLogMessage(logging.INFO, "Filtering data...", loggers)
        dfCovidForCounty = cvd.getFilteredData(chartingOptions["state"], chartingOptions["county"])

        if not dfCovidForCounty.empty:
            utl.processLogMessage(logging.INFO, "Computing daily deltas...", loggers)
            cvd.addComputedColumns(dfCovidForCounty)

            # dfCovidForCounty fields (columns) are: date,county,state,fips,cases,deaths
            pd.set_option("display.max_rows", None)
            utl.processLogMessage(logging.INFO, "\n" + str(dfCovidForCounty.tail()), loggers)

            cvd.showChart(
                dfCovidForCounty,
                chartingOptions["chartFocus"],
                chartingOptions["county"],
                chartingOptions["state"],
                chartingOptions["saveChart"],
            )


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
