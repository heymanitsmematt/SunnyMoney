from DataScraper.weather import Weather
from DataScraper.models import WeatherDay
from DataScraper.stocks import Stocker

#make requests for date range and save model data to database
w = Weather()
w.makeRequests('1997','2014')
w.saver()

#create a list of companies that will be used to populate the database
symbols = "BRK-A SEB NVR GOOG MA MKL ISRG WPO AAPL".split()

#and perform a search for the whole year range for each company's symbol
s = Stocker()
for sym in symbols:
    s.makeRequests('1997','2015',sym)
    s.saver()
