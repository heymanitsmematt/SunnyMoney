from django.db import models

class WeatherDay(models.Model):
    day = models.DateField()
    hail = models.BooleanField()
    snow = models.BooleanField()
    fog = models.BooleanField()
    rain = models.BooleanField()
    minTemp = models.IntegerField() #mintempi
    maxTemp = models.IntegerField() #maxtempi
    meanTemp = models.IntegerField() #meantempi
    minHumidity = models.IntegerField()
    maxHumidity = models.IntegerField()
    precipitation = models.IntegerField() #precipi
    snowfall = models.IntegerField() #snowfalli

    
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

