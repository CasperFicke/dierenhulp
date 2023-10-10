# nestkasten/forms.py

# django
from django import forms

# packages
from leaflet.forms.fields import PolygonField # django-leaflet

# local
from .models import Fourageergebied

# fourageergebiedfORM
class FourageergebiedForm(forms.ModelForm):
  geom = PolygonField()
  class Meta:
    model = Fourageergebied
    fields = ('name', 'geom')