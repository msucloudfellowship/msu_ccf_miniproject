# Getting Weather Data with Python

**Part of the [MSU Cloud Computing Fellowship Script Exercise](../readme.md)**

Before summarizing and visualizating weather data, you need to get some.  This program demonstrates and provides convenience functions
for using the excellent and totally free Meteostat system and python library.   For more information about Meteostat project see : https://meteostat.net

For more details about the Meteostat Python Library (in English) see : https://dev.meteostat.net/python/ 

## Usage of our data gathering script: 

First install the `meteostat` library if you haven't already.  You must have python 3.9 or higher installed

`pip -r requirements.txt`

or simply 

`pip install meteostat`


### usage example 1 - command line:

Meteostat pulls weather data from a weater station that you must specifcy.    It has a function (`Station()` ) for finding the ID of 
the nearest station.      This program has by default to pull 10 yrs data hourly weather from the station at Lansing Michigan Airport. 

Simply run from command line

`python fetch_weather_data.py`

Outcome: two new files `hourly_weather.csv` and `daily_weather.csv`

### usage example 2 - from Python:

To get from a different city, for example, Paris.  You'll need to run this from a python interpreter directly.  

start python in this folder, e.g. `python`

in the python interpreter, set the lat/lon to find nearest station, dates, and save 

example python session:

```
>>> from fetch_weather_data import *
>>> lat, lon = ( 1.290270 , 103.851959 )
>>> station = find_nearest_station(lat, lon)
>>> my_weather_file = "../data/hourly_weather_singapore.csv"
>>> get_and_save_hourly_weather_file(my_weather_file, station = station, start = datetime(2011, 1, 1), end = datetime(2021,12,31))
>>> exit()
```

If you use the suggested file name in the session above, a new file will be created in the 'data' folder.  You don't have to use this folder, 
and if you are saving data to a different location (different drive letter or volume), use that path.  


Note you could also add this code into a Python notebook that is started in this directory if you are familiar with how to start those. 