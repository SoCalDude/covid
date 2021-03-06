"""
**********************************************************************************************
test_covid19.py

Test harness script for the covid19 application.

J. Les Gainous
2020-05-17
**********************************************************************************************
"""
import sys
import unittest
import inspect
import datetime

sys.path.append(".")
import src.covid19 as cvd

c = cvd.Covid19()


class Test_Covid19(unittest.TestCase):
    def test_getLatestDataFalse(self):
        self.assertTrue(c.getLatestData(False), "{} failed".format(inspect.currentframe().f_code.co_name))

    def test_getTitleDateGood(self):
        strDate = "2020-05-24"
        self.assertEqual(
            c.getTitleDate(strDate),
            "May 24, 2020",
            "{} failed with {}".format(inspect.currentframe().f_code.co_name, strDate),
        )

    def test_getTitleDateBad(self):
        strDate = "1985-00-00"
        self.assertEqual(
            c.getTitleDate(strDate), "", "{} failed with {}".format(inspect.currentframe().f_code.co_name, strDate)
        )

    def test_reduceTicks(self):
        result1 = c.reduceTicks(500, 0.9)
        result2 = c.reduceTicks(0, 0.0)
        result3 = c.reduceTicks(-10, 0.5)
        result4 = c.reduceTicks(-150, -0.9)
        result5 = c.reduceTicks(2, 0.0000000001)
        result6 = c.reduceTicks(1, 0.0000000001)
        result7 = c.reduceTicks(0, 0.0000000001)

        assert (result1, result2, result3, result4, result5, result6, result7) == (50, 0, 0, 0, 2, 0, 0)

    def test_getFilenameTimestamp(self):
        self.assertEqual(c.getFilenameTimestamp(), datetime.datetime.now().strftime("%Y-%m-%d-%H%M"))


if __name__ == "__main__":
    unittest.main()
