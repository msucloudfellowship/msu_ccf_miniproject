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

The data is not included in this repository as it's not appropriate to store large files in github. 
However if you are part of the Cloud Fellowship you will be/have been sent a link to download a sample file from Lansing, MI.  Othwerwise, the data can be acquired from Meteostat's [bulk data service](https://dev.meteostat.net/bulk/), which requires a station ID.   The weather station closest to MSU is ID 72539 (Lansing aiport), and the URL to download a compressed data file is https://bulk.meteostat.net/v2/hourly/72539.csv.gz

This requires the program 'gunzip' to decompress into a CSV (I found the Mac archive program does not work, and windows unzip programs may not either).  Gunzip comes with Mac and can be used in the terminal, and for windows you may try to download and install WinZip.    

During the assignment we will provide an alternate URL to all Fellows to download the un-gzipped CSV from station #72539.  

### *Specifying the data file*

I tried to make it as flexible as possible to specify to the scripts (both Python and R) where to locate the data file.   You may put the file in the same folder, or leave it on a mounted disk (e.g. Z:\ or /mnt) if you connect cloud storage to your VM, or put it anywhere else on your computer (or VM), and with any name.  For details see the readme files in the R or Python folders. 

- The default is to look for a file called "hourly_weather.csv" in the same folder as the script.   You just run the program and it will work
- If you run from the command line you can specify the location as a command-line argument. See the instructions for each script.    Adjust for Windows vs Linux
- Alternatively, the scripts look for an environment variable with the name of the data file.   Setting the environment variable WEATHER_FILE before running the script and run without command line arguments it will use that find the file.   For example `../hourly_weather.csv` to use a file in this main directory, which is the parent directory to your script file.  

**Optional: Set environment variable in Windows cmd.exe :**

```
set WEATHER_FILE=..\hourly_weather.csv
```

if you mount an external drive (e.g. Azure File Share), you could similiarly use `set WEATHER_FILE=Z:\hourly_weather.csv`

**Optional: Set environment variable in Linux terminal**

```
export WEATHER_FILE=../hourly_weather.csv
```

For those that are very adventurous and want to try running these with containers, the Azure container instance has an option to set environment variables when the container is run.   If anyone is interested we can work on a Dockerfile for this project.  


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
