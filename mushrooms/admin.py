# stations/admin.py

# django
from django.contrib import admin

# packages
from leaflet.admin import LeafletGeoAdmin # django-leaflet

# local
from .models import MushroomSpot

# register Mushroomspot
admin.site.register(MushroomSpot, LeafletGeoAdmin)