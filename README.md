# covid
<div style="text-align: right;font-size: small">SoCalDude</div>  

---  
#### COVID-19 Charting for County

This is the COVID-19 charting application for displaying a chart of daily new COVID-19 cases (or daily COVID-19 deaths) for a particular county.

Currently, the data only shows for Orange County, California. The ability to choose any county from any state is forthcoming.

For the time being, if you wish to show a different county, please refer to the **Manual County Selection** section below. 

**Requirements**

- Python version 3.8 or later
- Internet Access (at least upon the first execution of the app). On subsequent executions, there is an option to use cached data
- Various third-party Python modules as listed in the _requirements.txt_ file
- Python application execution knowledge (teaching these Python basics are beyond the scope of this project)

**Setup and Launching the Application**

1. Run the _requirements.txt_ manifest file using one of the following terminal commands:

		pip install -r requirements.txt

	or

		python -m pip install -r requirements.txt
2. Run the main Python script from the _src_ folder:
    <br><pre>covid19oc.py</pre>
<br><br>

**Manual County Selection**
<br><br>
Review the [<ins>raw data file</ins>](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv) and search for your county. Once you have located an entry for your county, take note of the county ID. It is in the third logical position (fourth physical position) in the data line. This is also known as the _FIPS_ ID. Replace the value of the constant, TARGET_FIPS_ID, with this FIPS ID (leading zero is not necessary) in the file: <pre>src/config.py</pre>
