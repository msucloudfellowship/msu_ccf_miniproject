# weather_summary.R 
# plot summaries of weather data


# this script assumes data files are available in the current working directory
# Only Base R is required; no additional libraries need to be installed

read_weather <- function(weather_file) {
  print(paste("reading",weather_file))
  if(file.exists(weather_file)) {
    hourly_weather <- read.csv(weather_file)
  } else {
    warning(paste("weather file ", weather_file, "not found"))
    return(null)
  }
  
  names(hourly_weather) <- c("date","hour","temp","dwpt","rhum","prcp","snow","wdir","wspd","wpgt","pres","tsun","coco")
  return(hourly_weather)
}

#' weather_summary
#' 
plot_weather_summary <- function(hourly_weather,varname = 'temp', f = "min" ) {
  print(paste("summarizing and plotting",f, varname))

  x <- subset(hourly_weather, ! is.na(hourly_weather[varname]))
  x$year <- as.integer(format(as.Date(x$date, format="%Y-%m-%d"),"%Y") )
  x$week <- as.integer(format(as.Date(x$date, format="%Y-%m-%d"),"%W") )

  weather <- aggregate(x[varname], by=list(year=x$year, week=x$week), FUN=f)

  c = hcl.colors(max(weather$year) - min(weather$year) + 1, palette = "Sunset")


  main_title=paste(f, varname, "per week, colored by year")
  sub_title=paste(min(weather$year), "to", max(weather$year))
  plot(weather[[varname]] ~ weather[['week']], col=c, xlab="week", ylab = paste(f,"weekly",varname), 
       main = main_title, sub=sub_title)

}


main<-function(pdf_file="weather_plots.pdf"){
  pdf(pdf_file)
  weather_file <- Sys.getenv("WEATHER_FILE", unset="hourly_weather.csv")
  
  hourly_weather <- read_weather(weather_file)
  
  if (is.null(hourly_weather)){
    stop()
  }
  
  plot_weather_summary(hourly_weather,varname = "temp", "min")
  plot_weather_summary(hourly_weather,varname = "temp", "max")
  plot_weather_summary(hourly_weather,varname = 'prcp', "max")
  dev.off()
}

if (!interactive()) {
  main()
}

  
