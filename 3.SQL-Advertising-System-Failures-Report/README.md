<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
</head>

<body>
  <h1 align="center"> SQL: Advertising System Failures Report </h1>
</body>


## Description

As part of HackerAd's advertising system analytics, a team needs a list of customers who has a maximum number of failure events (status = "failure") in their campaigns. For all customers with more than 3 events with status = 'failure', report the customer name and their number of failures. The result should be in the following format: customer, failures.

- customer is a candidate's full name, the first_name and last_name separated by a single space.
- The order of the output is not important.

## Python Version used
This project was implemented and tested with Python 3.12.4 in a Windows 10 machine.

##  Step-by-step to execute it

To execute it, it is necessary to change variables with the informations of your own environment and for the Output desired.

The variable can be found at the beginning of the ````main.py```` file.

### Explaining variables

````commandline
#########INPUT#########
username = 'admin'
password = 'admin'
host = 'localhost'
database = 'mydb'
output = 'PROMPT' # Choose how the output will be shown: EXCEL or PROMPT
#######################
````

- ````username````: User to connect into the database
- ````password````: Password used to connect into the database
- ````host```` : Hostname which the database is installed
- ````database````: The database that will be used in this script
- ````output````: how the output must be shown. It can be "EXCEL" or "PROMPT". The EXCEL will generate an excel file while the PROMPT returns the results tabulated

### Execution

Go to the \<absolute path>\3.SQL-Advertising-System-Failures-Report\

Execute:

````commandline
python main.py
````
or
````commandline
python3 main.py
````

## Pre-requirements for the execution

To run this script, Python is necessary on the version described above. Also, the following Module will be needed:
- mysql-connector-python (command to install it ````pip install mysql-connector-python````)
- tabulate (command to install it ````pip install tabulate````)
- pandas openpyxl (command to install it ````pip install pandas openpyxl````)
