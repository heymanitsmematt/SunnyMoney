# SunnyMoney (note this project is in development and is not ready for the public yet...)
The sun and rain effect the stock market in ways that show how beautiful data is. 

This is a project to explore scikit-learn and build datasets through API.

I use the Django framework mostly because I like the file structure and it's quick to make a front end for this data once it's all collected, and the modeling helpes temendously when building your own models from raw data. 


# Data Collection
After some light perusing, I settled on wunderground and Yahoo as my API providers for this project. Yahoo has a great YQL querying language to structure for their database of historical stock information for most major players on the NYSE. Weather Underground also has a great free api (though limited to 10 requests/minute) with a plethora of data about each day requested. The simple api format is also helpful for both of these services, as I was able to get a couple loopers up and running to collect data in mere hours. 

The data is saved to a MySql database through django's model objects. In the DataScraper django app, the file constructDB.py uses mainly weather.py and stocks.py to populate the database for all dates available in associated data (5/1/1997-12/31/2014). Due to the limitation from Weather Underground, the database take about 7 hours to populate roughly 20 years of weather data. The Yahoo stocks data is much more friendly, as requests will return up to a year of data in one json package. 

After constructDB has been given plenty of peace and quiet to run, the data set will be available. (alternatively, the sql dumps file for that data set is in this repository as well). 




