# weather_summary.py

import pandas as pd
import sys,os
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


def read_weather(weather_file='hourly_weather.csv'):
  """read weather file, if found"""
  if not os.path.exists(weather_file):
    raise()

  try:  
    hourly_weather = pd.read_csv(weather_file, 
      names = ["date","hour","temp","dwpt","rhum","prcp","snow","wdir","wspd","wpgt","pres","tsun","coco"]
    )  
  except Exception as e:
    print("couldn't read weather file", e)
    
  return(hourly_weather)


def plot_weather_summary(hourly_weather, varname = 'temp', f = "min" ):
  """summarize weather data for variable name and generate plots
  """
  print(f"summarizing and plotting {f} {varname}")

  w = hourly_weather.dropna(subset=[varname])
  pd.options.mode.chained_assignment = None
  w['year'] = w['date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%Y"))
  w['week'] = w['date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%W"))
  pd.options.mode.chained_assignment = 'warn'
  weather = w.groupby(['year','week'], axis=0)[varname].agg(f).reset_index()

  sns.set_theme(style="whitegrid")
  g = sns.scatterplot(data=weather, x="week", y=varname, hue='year', palette="YlOrRd_r", legend=False ) # crest color palette
  
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
  hourly_weather = read_weather(weather_file)
  plot_weather_summary(hourly_weather, "temp", "min")
  plot_weather_summary(hourly_weather, "temp", "max")
  plot_weather_summary(hourly_weather, "prcp", "max")


if __name__ == "__main__":
  """If this file is run from command line, 
  read weather data and generate 3 plots"""

  # check if the data file was sent on the command line
  weather_files = ""
  if len(sys.argv) > 1:
    weather_file = sys.argv[1]
  else:
    weather_file = os.getenv("WEATHER_FILE")  or  "hourly_weather.csv"
  
  main(weather_file)






