# fetch_weather_data.py


Optional , not required to use for exercise
this code is not necessary to run, but is what I used to download the weather data to work with

## usage: 

First install the `meteostat` library (the only entry in `requirements.txt`)

`pip -r requirements.txt`


### usage example 1:
using all default (10 yrs data from Lansing), simply run from command line

`python fetch_weather_data.py`

Outcome: two new files `hourly_weather.csv` and `daily_weather.csv`

### usage example 2:
get from a different city, for example, Singapore

start python in this folder, e.g. `python`

in the python interpreter, set the lat/lon to find nearest station, dates, and save 

example python session:

```
>>> from fetch_weather_data import *
>>> lat, lon = ( 1.290270 , 103.851959 )
>>> station = find_nearest_station(lat, lon)
>>> get_and_save_weather_data(station,start = datetime(2011, 1, 1), end = datetime(2021,12,31), suffix = "_singapore" )
>>> exit()
```

Outcome:  two new files `hourly_weather_singapore.csv` and `daily_weather_singapore.csv`

