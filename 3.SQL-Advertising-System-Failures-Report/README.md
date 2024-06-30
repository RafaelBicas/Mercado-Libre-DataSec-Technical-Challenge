<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
</head>

<body>
  <h1 align="center"> SQL: Advertising System Failures Report </h1>
</body>


## Description

As part of HackerAd's advertising system analytics, a team needs a list of customers who have a maximum number of failure events (status = "failure") in their campaigns. For all customers with more than 3 events with status = 'failure', report the customer name and their number of failures. The result should be in the following format: customer, failures.

- customer is a candidate's full name, the first_name and last_name separated by a single space.
- The order of the output is not important.

## Python Version used
This project was implemented and tested with Python 3.12.4 in a Windows 10 machine.

##  Step-by-step to execute it

There are 2 ways of executing it. One of them is editing directly into the variable ````genre_desired```` at the beginning of the file or on the time of execution as a parameter.

### Editing the variable
````
###########INPUT##############
genre_desired = "Drama"
##############################
````
go to the \<absolute path>\2.REST-API-Best-TV-Shows-in-Genre\

execute:

````commandline
python main.py
````
or
````commandline
python3 main.py
````

### Passing as a parameter

Pass as a parameter a string which is related to the genre that will be searched.

````commandline
python .\main.py genre
````
or
````commandline
python3 .\main.py genre
````