import requests
from DataScraper.weather import Weather
from DataScraper.models import Company, StockDay
import sys
import datetime

#data exists in yahoo financial database api from 1996-05-01

class Stocker:
    def __init__(self):
        self.days = Weather().days
        self.results = dict()

    def makeRequests(self, startYear, endYear, symbol):
        ''' Makes requests to yahoo for the symbol and packs them into results dictionary for <str> startYear, endYear '''
        self.symbol = symbol
        if int(startYear)<1996:
            raise Exception("Yahoo API data only exists from 1996-05-01")

        #create a list of keys to build a results dict and search yahoo json response object
        keys = "Date High Low Open Close Adj_Close".split()

        # if we have more than one year span, requests will have to be made into yearly YQL queries
        if int(endYear) - int(startYear) > 1:
            #a request is built for each year in the range, and the results are stuffed into the results dict
            for year in range(int(startYear),int(endYear)):
                print year
                startDate = "%s-01-01" % year
                endDate = "%s-12-31" % year     
                self.url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20=%20%22" +symbol + "%22%20and%20startDate%20=%20%22" + startDate + "%22%20and%20endDate%20=%20%22" + endDate + "%22&format=json&diagnostics=true&env=store://datatables.org/alltableswithkeys"
                r = requests.get(self.url)
                data = r.json()
                
                try:
                    # results are stored in a list nested in the yahoo API json response object
                    for result in data['query']['results']['quote']:
                        resultDataDict = dict()
                        k = 0
                        
                        #iterate through the keys and assign each day's results to the results dictionary
                        while k < len(keys):
                            key, val = keys[k], result[keys[k]]
                            resultDataDict[key] = val
                            k += 1
                        self.results[resultDataDict['Date']] = resultDataDict
                except:
                    self.data = data
                    print "err?", sys.exc_info()[0]

        # otherwise this is only a one year gap and YQL will return that range
        else:      
            startDate = "%s-01-01" % startYear
            endDate = "%s-12-31" % endYear
            self.url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20=%20%22" +symbol + "%22%20and%20startDate%20=%20%22" + startDate + "%22%20and%20endDate%20=%20%22" + endDate + "%22&format=json&diagnostics=true&env=store://datatables.org/alltableswithkeys"
            r = requests.get(self.url)
            data = r.json()
            
            try:
                # results are stored in a list nested in the yahoo API json response object
                for result in data['query']['results']['quote']:
                    resultDataDict = dict()
                    k = 0
                    
                    #iterate the single year's results and construct that year's results dictionary
                    while k < len(keys):
                        key, val = keys[k], result[keys[k]]
                        print key, val
                        resultDataDict[key] = val
                        k += 1
                    self.results[resultDataDict['Date']] = resultDataDict
            
            except:
                self.data = data
                print "err?", sys.exc_info()[0]

    def saver(self):
        '''save results to the db for each day returned in the results, creating or updating the records extant'''
        for day in self.results:
            #reference day dict object in all results for less typing later
            res = self.results[day]
                    
            #get the company reference so we know who these results will be assigned to
            thisCompany = Company.objects.get_or_create(symbol = self.symbol)[0]

            #split the date results so this can be turned into a datetime object
            yr, mo, da = day.split("-")
            thisDay = datetime.date(int(yr), int(mo), int(da))

            #begin creating result object to save
            stockDay = StockDay.objects.create(day = thisDay, company = thisCompany)
            stockDay.high = float(res['High'])
            stockDay.low = float(res['Low'])
            stockDay.open = float(res['Open'])
            stockDay.close = float(res['Close'])
            stockDay.adjClose = float(res['Adj_Close'])

            #finally save both the company and stock day objects
            stockDay.save()
            thisCompany.save()
            print "saved %s to the company %s" % (day, self.symbol)

''' for testing, will search yahoo for a two year span automatically
s = Stocker()
s.makeRequests('2001','2003','YHOO')
s.saver()
'''
