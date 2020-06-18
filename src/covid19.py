# region Imports
import datetime
import os.path
import shutil
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import sys
import traceback

sys.path.append(".")
import src.config as cfg

from PyQt5 import QtCore, QtGui, QtWidgets, uic

# import mainFormConfig as formCfg
from src.mainForm import Ui_MainWindow

# endregion


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # custom property settings
        self.setFixedSize(374, 195)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        # custom event handling (assigning slots)
        self.btnStart.clicked.connect(self.handleStartButton)
        self.btnClose.clicked.connect(self.handleCloseButton)

    def handleStartButton(self) -> None:
        try:
            self.btnStart.setEnabled(False)
            self.btnClose.setEnabled(False)
            launchOptions = {"isFromServer": self.radServerData.isChecked(), "saveChart": self.chkSavePlotImage.isChecked()}
            launchCharting(launchOptions)
        except:
            print(f"An error occurred: {sys.exc_info()[0]}; {sys.exc_info()[1] if len(sys.exc_info()) > 1 else ''}\n{traceback.format_exc()}")
        finally:
            self.btnStart.setEnabled(True)
            self.btnClose.setEnabled(True)

    def handleCloseButton(self):
        self.close()


class Covid19:
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
                    print(
                        f"Unable to retrieve data from server. HTTP status code: {csv.status_code}. Using local data, if possible."
                    )
            except Exception as ex:
                print(f"The following error occurred. '{ex.__doc__}'. Using local data, if possible.")
                retVal = False

            # when the call succeeds and there is some text then
            # make a copy of the old file and create the new one
            if retVal and wasRemoteCallSuccessful:
                try:
                    if os.path.exists(cfg.LOCAL_FILE):
                        shutil.copy(cfg.LOCAL_FILE, cfg.LOCAL_FILE + ".prev")

                    with open(cfg.LOCAL_FILE, "w") as f:
                        f.write(csv.text)
                except Exception as ex:
                    print(f"The following error occurred. '{ex.__doc__}'")
                    retVal = False

        return retVal

    def getFilteredData(self, fipsID: float) -> pd.DataFrame:
        dfOC: pd.DataFrame = None

        try:
            df = pd.read_csv(cfg.LOCAL_FILE, delimiter=None, encoding="mbcs")
        except Exception as ex:
            print(f"Unable to read local data, '{cfg.LOCAL_FILE}'. {ex.__doc__}")
        else:
            # filter just for the  requested fips value. When the dataframe was created,
            # fips was imported as a float64
            dfOC = df[df.apply(lambda f: f["fips"] == fipsID, axis=1)]
            dfOC = dfOC.drop(cfg.UNUSED_COLUMNS, axis=1)

        return dfOC

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

        print(f"Using {tickCount} with a {percentReduction} reduction, reduceTicks() returned {retVal}")
        return retVal

    # converts a string representation of a date to a specifically formatted string date for the graph title
    def getTitleDate(self, dateString: str) -> str:
        stringDate: str = ""
        try:
            stringDate = format(datetime.datetime.strptime(dateString, "%Y-%m-%d").strftime("%B %d, %Y"))
        except ValueError as ve:
            stringDate = ""

        return stringDate

    def getFilenameTimestamp(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d-%H%M")

    def showChart(self, df: pd.DataFrame, whichMetric: cfg.ChartFocus, saveChart: bool) -> None:
        yAxis: str = ""
        yLabel: str = ""

        df = df.set_index("date")

        if whichMetric == cfg.ChartFocus.NEW_CASES:
            yAxis = "NewCases"
            yLabel = "New Cases per Day"
        elif whichMetric == cfg.ChartFocus.NEW_DEATHS:
            yAxis = "NewDeaths"
            yLabel = "Deaths per Day"

        plt.figure(figsize=(10, 5))
        # Add main data to the graph
        plt.plot(df[yAxis], label=yLabel)
        # Add the moving average to the graph
        plt.plot((df.SMAc if whichMetric == cfg.ChartFocus.NEW_CASES else df.SMAd), label="14-Day Moving Avg")

        # show every x ticks
        plt.xticks(np.arange(0, len(df.index), self.reduceTicks(len(df.index), cfg.TICK_REDUCTION_FACTOR)))

        # set the graph's other appearance properties
        plt.title(
            "Orange Co. Covid-19\n(from {} to {}, inclusive)".format(
                self.getTitleDate(df.index[0]), self.getTitleDate(df.index[len(df.index) - 1])
            )
        )

        plt.xticks(fontsize=7, rotation=45, ha="right")
        plt.grid(axis="x", which="major", color="#E5E5E5", linestyle="dotted")
        plt.grid(axis="y", which="major", color="#E5E5E5", linestyle="solid")
        plt.legend()

        # if saving the chart is requested
        if saveChart:
            plt.savefig(cfg.CHART_FILENAME.format(self.getFilenameTimestamp()), bbox_inches="tight")

        # display chart
        plt.show()


def launchCharting(chartingOptions: dict) -> None:
    cvd = Covid19()
    useServerData = chartingOptions["isFromServer"]

    # this was chosen by the user in the GUI if they want fresh data or not
    print("Retrieving data from server..." if useServerData else "Retrieving from local file...")
    if (not cvd.getLatestData(useServerData)) and (not os.path.isfile(cfg.LOCAL_FILE)):
        print("Unable to download latest data nor able to use local data.")
    else:
        print("Filtering data...")
        dfOC = cvd.getFilteredData(cfg.TARGET_FIPS_ID)

        if not dfOC.empty:
            print("Computing daily deltas...")
            cvd.addComputedColumns(dfOC)

            # dfOC fields (columns) are: date,county,state,fips,cases,deaths
            pd.set_option("display.max_rows", None)
            print(dfOC.tail())

            cvd.showChart(dfOC, cfg.ChartFocus.NEW_CASES, chartingOptions["saveChart"])


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
