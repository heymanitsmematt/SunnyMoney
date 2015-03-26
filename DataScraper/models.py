from django.db import models

class WeatherDay(models.Model):
    day = models.DateField()
    hail = models.BooleanField(null=True)
    snow = models.BooleanField(null=True)
    fog = models.BooleanField(null=True)
    rain = models.BooleanField(null=True)
    minTemp = models.IntegerField(null=True) #mintempi
    maxTemp = models.IntegerField(null=True) #maxtempi
    meanTemp = models.IntegerField(null=True) #meantempi
    minHumidity = models.IntegerField(null=True)
    maxHumidity = models.IntegerField(null=True)
    precipitation = models.IntegerField(null=True) #precipi
    snowfall = models.IntegerField(null=True) #snowfalli

    
class Company(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True)

class StockDay(models.Model):
    day = models.DateField()
    company = models.ForeignKey(Company)
    high = models.FloatField(null=True)  
    low = models.FloatField(null=True)   
    open = models.FloatField(null=True)  
    close = models.FloatField(null=True) 
    adjClose = models.FloatField(null=True)  #Adj_Close

