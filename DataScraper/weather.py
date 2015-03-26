import requests
import sys
import time
import datetime
from DataScraper.models import WeatherDay

class Weather:
    def __init__(self):
        #build a list of YYYYMMDD for each year in the range. 
        self.days = list()
        for year in range(1980, 2015):
            #for each month in the year, 
            for m in range(1,13):
                #if the month has 31 days
                if m in (1,3,5,7,8,10,12):
                    #comine the year the formatted month and date into strings of at least two digit integers
                    for num in range(1,32):
                        ystr = str(year) + "%s%s" %  ("%02d" % (m,),"%02d" % (num,))
                        self.days.append(ystr)
                #if the month has 30 days
                if m in (4,6,9,11):
                    for num in range(1,31):
                        ystr = str(year) + "%s%s" % ("%02d" % (m,),"%02d" % (num,))
                        self.days.append(ystr)
                #february...
                if m == 2:
                    if year in (range(1980, 2015, 4)):
                        for num in range(1,29):
                            ystr = str(year) + "%s%s" % ("%02d" % (m,),num)
                            self.days.append(ystr)
                    else:
                        for num in range(1,29):
                            ystr = str(year) + "%s%s" % ("%02d" % (m,),num)
                            self.days.append(ystr)
                m += 1

    def makeRequests(self, yearStart, yearEnd):
        ''' Accepts yearStart, yearEnd <str> YYYY '''
        #object for inspecting results
        self.results = dict()

        #filter all days dictionary to results in set
        self.searchDays = [d for d in self.days if d[:4] == yearStart or d[:4]== yearEnd]

        #list of keys for dict returned to save values to database
        keys = "hail snow fog rain mintempi maxtempi meantempi minhumidity maxhumidity precipi precipsource snowfalli".split()
        
        p = 1
        for day in self.searchDays:
            thisDayDict = dict()
            k=0
            try:
                #send a request for every day in the searchDays range
                url = "http://api.wunderground.com/api/6cc11b3df8b5c1b9/history_%s/q/NY/Manhattan.json" % day
                r = requests.get(url)
                self.data = r.json()
                
                #build dict for each key in keys object
                while k<len(keys):
                    key, val = keys[k], self.data['history']['dailysummary'][0][keys[k]]
                    thisDayDict[key] = val
                    k += 1

                #add the constructed dictionary for this day to the master dictionary
                self.results[day] = thisDayDict
                print "request successful for %s" % day

            except:
                print 'err?', sys.exc_info()[0], day, k
            
            print "sleeping for the %sth time" % p
            p += 1
            time.sleep(5.5)

    def saver(self):
        ''' This function saves all results to the database '''

        for day in w.results:
            #create datetime.date object and get/create db object for that day
            thisDay = datetime.date(int(day[:4]), int(day[4:6]), int(day[6:8]))            
            thisDay = WeatherDay.objects.get_or_create(day=thisDay)[0]
        
            #build object of results to save time accessing later
            results = w.results[day]

            #assign the results to the proper data fields
            thisDay.hail = results['hail']
            thisDay.snow = results['snow']
            thisDay.fog = results['fog']
            thisDay.minTemp = results['mintempi']
            thisDay.maxTemp = results['maxtempi']
            thisDay.meanTemp = results['meantempi']
            thisDay.minHumidity = results['minhumidity']
            thisDay.maxHumidity = results['maxhumidity']
            thisDay.precipitation = results['precipi']
            thisDay.snowfall = ['snowfalli']

            #finally save this day to the database
            thisDay.save()
            print "saved %s to the database!!!" % day

''' some fun for testing
start = raw_input("what is your start year? ")
end = raw_input("what is your end year? ")

w = Weather()
w.makeRequests(start, end)
w.saver()
'''



        
