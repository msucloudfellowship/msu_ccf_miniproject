# Simple Weather Data Plotting Scripts

**For MSU Cloud Computing Fellowship Exercise**

## Overview

These are the scripts to be run for an exercise in the [MSU Cloud Computing Fellowship](https://msu-icer.github.io/cloudcomputingfellowship).  The goal of the exerciseis to demonstrate copying data to the cloud, and using cloud computing to run a basic script, save the output to cloud storage.    The steps we have in mind to work through are: 

1. find a source of data you can use code to download
2. create storage and compute resources in the cloud
3. get these scripts into the compute resource
4. run the data gathering script on the compute resource to pull data (CSV) and store into cloud storage
5. 

#### Skill level

This exercise does not require you to 

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


## BONUS POINTS! 

There are different types of cloud storage with different pricing tiers from all cloud providers.   Azure has a 'files' or 'File Share' option which is easily connected to a windows or linux Virtual Machine.   However the cheapest and cloudiest option is what Azure calls 'blob' storage and the others call 'object' storage.    It's not the same as a file server in your company's data center, or the external drive you connect.   The best way to access object storage is with code. 

The 'fetch weather data' script simply saves a file to CSV.  This then needs to be copies to to cloud storage for the exercise, or to save it cheaply.   How can you acheive this?   Which methods would work if you wanted to analyze across thousands of locations?

 - download on your laptop, then use a program or the cloud web interface to upload to storage.   
 - download on your laptop, but use the storage web API to upload (e.g with CURL or other)
 - connect the storage to the VM (in Azure, you can mount azure files to a VM), then on the VM download the file and copy over the mounted connection
 - for thousands of files, repeat any of the above, requires using Azure files tier and mounting file shares
 - instead of saving to CSV, use the Azure software development key (SDK) to add lines of code that saves directly to cloud storage from your program.   requires only Blob storage and container 