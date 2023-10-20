"""
fetch_weather_data 
Optional , not required to use for exercies
this code is not necessary to run, but is what I used to download the weather data to work with

usage: 
1. using all default (10 yrs data from Lansing, simply run in a python interpreter

python fetch_weather_data.py

2. get from a different city, for example, paris
in python
>>> from fetch_weather_data import *
>>> lat, lon = ( 48.864716, 2.349014 ) 
>>> station = find_nearest_station(lat, lon)
>>> get_and_save_weather_data(station,start = datetime(2000, 1, 1), end = datetime(2022,12,31), suffix = "_paris" )
>>> exit()

two files will be created: "daily_weather_singapore.csv" and "hourly_weather_singapore.csv"

If you want to simply pull weather data into a variable, use the methods from the meteostat package directly  
eg daily = Daily(station, start, end).fetch()
)
"""

from datetime import datetime
from meteostat import Stations, Daily,Hourly

# Michigan State University (42.729660, -84.481534)
def find_nearest_station(lat=42.729660, 
                         lon=-84.481534, 
                         start = datetime(2011, 1, 1), 
                         end = datetime(2021,12,31)):
  """Wrapper around the meteostat Station() function providing default values for 
  a station near Michigan State University (which turns out to be Lansing Airport)

  see https://dev.meteostat.net/python/stations.html#example for details
 
  Args:
      lat (float, optional): Latitude used to search for station. Defaults to 42.729660.
      lon (float, optional): Longitude used to search for station. Defaults to -84.481534.
      start (datetime, optional): Start date for when we would like to find weather, looks for a station that has data from this period. Defaults to datetime(2011, 1, 1).
      end (datetime, optional): Start date for when we would like to find weather, looks for a station that has data from this period. Defaults to datetime(2021,12,31).
  """

  # get all stations
  stations = Stations()
  # set filters on stations for those near campus with daily weather available
  stations = stations.nearby(lat, lon)
  stations = stations.inventory('daily', (start, end))
  stations = stations.inventory('hourly', (start, end))

  # get the station at the top of the list (for East Lansing, this is lansing capital airport)
  station = stations.fetch(1)
  return(station)

def get_and_save_hourly_weather_file(
    hourly_file_path = '../data/hourly_weather.csv', 
    station=find_nearest_station(), 
    start = datetime(2011, 1, 1), 
    end = datetime(2021,12,31)
    ):
  
  """ save hourly and daily weather to csv files. 
  This is mostly a convenience wrapper with reasonable default values for the meteostat.Hourly() function

  This has the side effect: writes files to disk.  If you want to pull data into memory, just use the meteostat 
  package 'Hourly()' function directly in your code

  Args:
      station (meteostat station object): Meteogram station object, default is from find_nearest_station function above
      start (datetime, optional): Start date of weather data. Defaults to datetime(2011, 1, 1).
      end (datetime, optional): End date of weather data, occurring after start. Defaults to datetime(2021,12,31).
      returns: Boolean T if pull and write was successful. 
  """
  
  try:    
    #define hourly object and fetch all data
    hourly_data = Hourly(station, start, end).fetch()
    hourly_data.to_csv(hourly_file_path)
    print(f"hourly weather saved to {hourly_file_path}")
  except Exception as e:
    print("weather file writing error:", e)
  return(True)


# this is a previous version that is not longer used.  

def get_and_save_weather_data(station=find_nearest_station(), 
              start = datetime(2011, 1, 1), 
              end = datetime(2021,12,31), 
              suffix = ""):
  """ save hourly and daily weather to csv files
  station : Meteogram station object
  start : datetime object
  end : datetime object, > start
  returns: 
  side effect: writes files to disk"""
  
  try:
    daily_data = Daily(station, start, end).fetch()
    daily_file = f"daily_weather{suffix}.csv"
    daily_data.to_csv(daily_file)
    print(f"daily weather saved to {daily_file}")
    
    #define hourly object and fetch all data
    hourly_file = f"hourly_weather{suffix}.csv"
    hourly_data = Hourly(station, start, end).fetch()
    hourly_data.to_csv(hourly_file)
    print(f"hourly weather saved to {hourly_file}")
  except Exception as e:
    print("weather file writing error:", e)
  
  return(True)

if __name__ == "__main__":
  get_and_save_hourly_weather_file()
