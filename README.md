# Python
BSE publishes a "Bhavcopy" file every day here: http://www.bseindia.com/markets/equity/EQReports/BhavCopyDebt.aspx?expandable=3

Python script that:
- Downloads the Equity bhavcopy zip from the above page
- Extracts and parses the CSV file in it
- Writes the records into Redis into appropriate data structures
(Fields: code, name, open, high, low, close)

Also, REST APIs are created to access these values.

the file app.py gives a very simple rest api using python flask.
