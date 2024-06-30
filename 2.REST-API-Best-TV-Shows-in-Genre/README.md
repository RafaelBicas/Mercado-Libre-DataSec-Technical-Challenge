<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
</head>

<body>
  <h1 align="center"> REST API Best TV Shows in Genre </h1>
</body>


## Description

Use the HTTP GET method to retrieve information about recent television shows. Query https://jsonmock.hackerrank.com/api/tvseries to find all the shows in a genre. The query result is paginated. To access additional pages, append ?page={num} to the URL where num is the page number.

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

 <h2> Use example 📸 </h2>

<p align="center">
  <img src="https://github.com/RafaelBicas/Mercado-Libre-DataSec-Technical-Challenge/tree/main/2.REST-API-Best-TV-Shows-in-Genre/Pictures/use_case.png" alt="Using the script to return the result related to 'mystery'" width="500">
</p>