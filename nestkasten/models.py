# nestkasten/models.py

# django
from django.db import models

# django packages
from djgeojson.fields import PointField, PolygonField

# Nestkast model
class Nestkast(models.Model):
  class Meta:
    verbose_name        = 'Nestkast'
    verbose_name_plural = 'Nestkasten'
  # attributes
  name        = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  geom        = PointField(blank=True, null=True)
  
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.name}' # - lat: {self.latitude} - long: {self.longitude}

# Fourageergebied model
class Fourageergebied(models.Model):
  class Meta:
    verbose_name        = 'Fourageergebied'
    verbose_name_plural = 'Fourageergebieden'
  # attributes
  name        = models.CharField(max_length=256)
  description = models.TextField(blank=True, null=True)
  picture     = models.ImageField(blank=True)
  geom        = PolygonField()

  def __str__(self):
    return self.name

  @property
  def picture_url(self):
    return self.picture.url