# nestkasten/admin.py

# django
from django.contrib.gis import admin

# packages
from leaflet.admin import LeafletGeoAdmin # django-leaflet

# local
from .models import Nestkast, Fourageergebied

# marker model
admin.site.register(Nestkast, admin.GISModelAdmin)
  

# register Fourageergebied
admin.site.register(Fourageergebied, LeafletGeoAdmin)