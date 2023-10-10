# mushrooms/admin.py

# django
from django.contrib import admin

# packages
from leaflet.admin import LeafletGeoAdmin # django-leaflet

# local
from .models import MushroomSpot
from .forms import PointEntryOrSelectForm

# register Mushroomspot
#admin.site.register(MushroomSpot, LeafletGeoAdmin)

@admin.register(MushroomSpot)
class MushroomSpotAdmin( LeafletGeoAdmin):
  form = PointEntryOrSelectForm
