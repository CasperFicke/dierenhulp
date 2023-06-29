# mushrooms/models.py

# django
from django.db import models

# django packages
from djgeojson.fields import PointField

# Mushroomspot model
class MushroomSpot(models.Model):
  name        = models.CharField(max_length=256, blank=True, null=True)
  geom        = PointField()
  description = models.TextField(blank=True, null=True)
  picture     = models.ImageField(blank=True, null=True)
  
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.name
  
  @property
  def popupContent(self):
    return '<img src="{}" /><p><{}</p>'.format(
      self.picture.url,
      self.description)