""" weather_summary.py
read in weather csv file and plot summaries of data by week
to get weather data, see fetch_weather_data.py 
"""

import pandas as pd
import sys,os
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns



# example data from the meteostat package
# hourly
# time,temp,dwpt,rhum,prcp,snow,wdir,wspd,wpgt,pres,tsun,coco
# 2011-01-01 00:00:00,10.0,9.4,96.0,,,170.0,11.2,,1010.2,,
# daily
# time,tavg,tmin,tmax,prcp,snow,wdir,wspd,wpgt,pres,tsun
# 2011-01-01,3.9,-6.7,12.2,3.0,0.0,229.0,27.4,,1009.6,


def read_weather(weather_file='hourly_weather.csv'):
  """read weather file into pandas data frame, works with either hourly or daily data from meteo stat (or any csv file with time in it)"""
  if not os.path.exists(weather_file):
    raise FileNotFoundError(f"weather file {weather_file} not found")

  # read in weather file with any set of columns, excpet assuming first column is a datetime string
  # convert first column string to datetime object
  try:  
    weather_df = pd.read_csv(weather_file, parse_dates=[0] )
      
  except Exception as e:
    print(f"couldn't read weather file as csv {weather_file}:", e)
    
  return(weather_df)


def plot_weather_summary(weather_df, varname = 'temp', f = "min" ):
  """summarize weather data for variable name and generate plots, 
  using from the meteostat package

  parameters
  
  weather_df : pandas data frame with first column named 'time' in datetime format
  varname : the name of the column to summarize over time, must be in the data frame.   
  f : the summary method/function to use on the plot, must be a valid python function that takes a single numeric input (min, max, avg)

  """

  if varname not in weather_df.columns: 
    raise ValueError('column varname not in data frame ')

  print(f"summarizing and plotting {f} {varname}")

  
  # remove missing data, which come up as NA when read in
  w = weather_df.dropna(subset=[varname])

  # create new columns for year and week number to summarize over
  # assumes there is a column 'time' (the column name from the meteostat package) and that is has datetime data type
  # tell pandas we don't want to change the time column but just add new columns
  pd.options.mode.chained_assignment = None

  w['year'] = w['time'].apply(lambda x: x.strftime("%Y"))
  w['week'] = w['time'].apply(lambda x: x.strftime("%W"))

  # set pandas option back to normal
  pd.options.mode.chained_assignment = 'warn'

  # weather = w.groupby(['year','week'], axis=0)[varname].agg(f).reset_index()
  weather = w.groupby(['year','week'])[varname].agg(f).reset_index()

  # sns.set_theme(style="whitegrid")
  g = sns.scatterplot(data=weather, x="week", y=varname, palette="YlOrRd_r", hue="year", legend=False ) # crest color palette
  
  g.set(xlabel="week number",
       ylabel=f"{f} weekly {varname}",
       title=f"{f} {varname} per week, colored by year")

  g.xaxis.set_major_locator(ticker.MultipleLocator(5))  
  g.xaxis.set_major_formatter(ticker.ScalarFormatter())
  fig = g.get_figure()
  fig.savefig(f"{f}_{varname}_weekly.png")
  plt.close()

def main(weather_file='hourly_weather.csv'):
  """ read in weather file and generate 3 basic plots"""
  weather_df = read_weather(weather_file)
  plot_weather_summary(weather_df, "temp", "min")
  weather_df = read_weather(weather_file)
  plot_weather_summary(weather_df, "temp", "max")
  weather_df = read_weather(weather_file)
  plot_weather_summary(weather_df, "prcp", "max")


if __name__ == "__main__":
  """If this file is run from command line, 
  read weather data and generate 3 plots
  
  command line usage A: 
  python weather_summary.py /path/to/weather_file.csv
  
  command line usage B:
  export WEATHER_FILE='/path/to/weather_file.csv'
  python weather_summary.py 
  """

  # check if the data file was sent on the command line
  weather_files = ""
  if len(sys.argv) > 1:
    weather_file = sys.argv[1]
  else:
    weather_file = os.getenv("WEATHER_FILE")  or  "hourly_weather.csv"
  
  main(weather_file)


