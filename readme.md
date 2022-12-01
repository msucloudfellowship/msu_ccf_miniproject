# Simple Weather Data Plotting Scripts

**For use with the the MSU Cloud Fellowship mini-project**

## Overview

These are the scripts to be run as part of the MSU Cloud Fellowship "mini project."  The goal of the mini-project is to demonstrate copying data to the cloud, and using cloud computing to run a basic script, save the output to cloud storage.  

## Scripts

There are two scripts here in an Python and R folder.   Each works with the data file that will be provided, and requires you to set an Environment variable if you run the script on the command line.   They each attempt to save 3 plots to disk, which are similar but not the same plot or file format (R saves a PDF, Python saves PNG files).     

## Requirements

See the instructions in the `readme.md` file in each folder for specific installation requirements and how to run.  

For both of these, the MS Azure "Data Science VM" does have nearly all the requirements to run.   The Python script does requires additional libraries to be installed on this VM.  Other VMs or Containers (e.g. plain Linux) will require additional Python or R software to be installed.  

## Data

Data the scripts work with is hourly weather observations from the [Meteostat project](https://meteostat.net/en/) which makes weather data freely available.  This has the following columns, but no column header: 

"date","hour","temp","dwpt","rhum","prcp","snow","wdir","wspd","wpgt","pres","tsun","coco"

The data can be acquired from their [bulk data service](https://dev.meteostat.net/bulk/) if you know the station name.   The weather station closest to MSU is ID 72539 (Lansing aiport), and the The URL for this file is https://bulk.meteostat.net/v2/hourly/72539.csv.gz

This requires the program 'gunzip' to decompress into a CSV (Mac and windows unzip programs may not work).  

During the assignment we will provide an alternate URL to download the un-gzipped CSV from station #72539.  

## *Specifying the data file*

The scripts look for an environment variable with the name of the data file, and if not found assume the data file is named `hourly_weather.csv` in the same directory as the script.  You can use a different filename or path by setting the variable WEATHER_FILE before running the script.    In this way you can reference the data file on a mounted drive (e.g. Z:\ ) or different directory. 

For example, to use a file in this maim directory, which is the parent directory to your script file

**In Windows cmd.exe window**


```
set WEATHER_FILE=..\hourly_weather.csv
```

if you mount an external drive (e.g. Azure File Share), you could similiarly use `set WEATHER_FILE=Z:\hourly_weather.csv`

**In Linux terminal**

```
export WEATHER_FILE=../hourly_weather.csv
```



