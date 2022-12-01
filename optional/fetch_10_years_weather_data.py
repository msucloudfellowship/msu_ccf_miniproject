## Optional 
# this code is not necessary to run, but is what I used to download the weather data to work with

from datetime import datetime
from meteostat import Stations, Daily,Hourly

def find_nearest_station(lat, lon, start = datetime(2011, 1, 1), end = datetime(2021,12,31)):
  # get all stations
  stations = Stations()
  # set filters on stations for those near campus with daily weather available
  stations = stations.nearby(lat, lon)
  stations = stations.inventory('daily', (start, end))
  stations = stations.inventory('hourly', (start, end))

  # get the station at the top of the list (for East Lansing, this is lansing capital airport)
  station = stations.fetch(1)
  return(station)


lat, lon = 42.734722, -84.480556
start = datetime(2011, 1, 1)
end = datetime(2021,12,31)
station = find_nearest_station(lat, lon, start, end)

def save_data(station, start, end, suffix = ""):
  """ save hourly and daily weather to csv files
  station : Meteogram station object
  start : datetime object
  end : datetime object, > start
  returns: 
  side effect: writes files to disk"""
  
  try:
    daily_data = Daily(station, start, end).fetch()
    daily_data.to_csv(f"daily_weather{suffix}.csv")

    #define hourly object and fetch all data
    hourly_data = Hourly(station, start, end).fetch()
    hourly_data.to_csv(f"hourly_weather{suffix}.csv")
  except Exception as e:
    print("weather file writing error:", e)
  
  return(True)

