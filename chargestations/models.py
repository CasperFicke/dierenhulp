# chargestations/models.py

from django.db import models

# Chargestation model
class EVChargingLocation(models.Model):
  station_name = models.CharField(max_length=250)
  latitude     = models.FloatField()
  longitude    = models.FloatField()

  def __str__(self):
    return self.station_name

# Userlocation model
class UserLocation(models.Model):
  location_name = models.CharField(max_length=100)
  latitude      = models.FloatField()
  longitude     = models.FloatField()

  def __str__(self):
    return self.location_name