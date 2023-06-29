# nestkasten/admin.py

# django
from django.contrib import admin

# packages
from leaflet.admin import LeafletGeoAdmin # django-leaflet

# local
from .models import Nestkast, Fourageergebied

# register Mushroomspot
admin.site.register(Nestkast, LeafletGeoAdmin)

# register Fourageergebiesd
admin.site.register(Fourageergebied, LeafletGeoAdmin)