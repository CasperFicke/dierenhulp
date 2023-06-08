# nestkasten/models.py

"""Markers models."""

#from django.contrib.gis.db.models import PointField
from django.db import models

class Nestkast(models.Model):
  """A marker with name and location."""
  class Meta:
    verbose_name        = 'Nestkast'
    verbose_name_plural = 'Nestkasten'
  # attributes
  name = models.CharField(max_length=255)
  #location = PointField()
  
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.name}' # - lat: {self.latitude} - long: {self.longitude}
   