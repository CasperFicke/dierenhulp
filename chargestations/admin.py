# chargestations/admin.py

# django
from django.contrib import admin

# local
from .models import EVChargingLocation, UserLocation

# Register EVstation
admin.site.register(EVChargingLocation)

# Register user
admin.site.register(UserLocation)