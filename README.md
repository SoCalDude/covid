![covid Charting Project logo](https://github.com/SoCalDude/covid/blob/master/images/covid-image-120x123.png)
# covid Charting Project
<div style="text-align: right;font-size: small">SoCalDude</div>  

---  
#### COVID-19 Charting for County

![COVID-19 New Cases Screenshot](https://github.com/SoCalDude/covid/blob/master/images/screenshot-01.png)

This is the COVID-19 charting application for displaying a chart of daily new COVID-19 cases (or daily COVID-19 deaths) for a particular county in the United States.


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

**The Main Window**

![COVID-19 Main Window Screenshot](https://github.com/SoCalDude/covid/blob/master/images/screenshot-03.png)
<br><br>

1. Choose a state from the drop-down list of states.

    These are populated with each state of the United States, along with U.S. territories.
2. Choose a county from the drop-down list of counties.

    The counties are populated based on the currently selected state.
3. Choose what metric you would like charted.

    Your choices are "daily new cases" or "daily new deaths"
4. Choose your source of the data.

    - Select "internet" if you want the latest data.
	
	_NOTE_: This is mandatory if this is the first time the application has not run.
	
	- Select "local previous data" if you want to rerun the charting on the same day it has been run before. 
	
	The internet data is only updated once a day, so using local previous data is faster for subsequent charting on the same day.
5. Indicate whether the chart image is automatically saved once it is displayed on the screen.

    The chart is saved in the subfolder named "chart" under the main application folder. 
	
	The naming convention of these saved charts is one of the following:
	
	>covid-19-new-cases-\{cntyname\}-county-\{stname\}-YYYY-MM-DD-HHmm.png
	>
	>covid-19-new-deaths-\{cntyname\}-county-\{stname\}-YYYY-MM-DD-HHmm.png
	
	where:
	
	    {cntyname} = county's name
		{stname} = state's name
		YYYY = four-digit year
		MM = two-digit month
		DD = two-digit day
		HH = hour (24-hour clock)
		mm = two-digit minutes
		
	_All date and time information is the date and time the chart was created and saved_
6. Press the "Start" button to retrieve, process, and chart the data.

    _NOTE_: The choices and button on the main window are disabled when the chart is displayed. Closing the chart reenables the main window of the application.
	
	![COVID-19 New Deaths Screenshot](https://github.com/SoCalDude/covid/blob/master/images/screenshot-04.png)
7. Press the "Close" button to exit the application.


