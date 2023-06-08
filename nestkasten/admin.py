# nestkasten/admin.py

# django
from django.contrib import admin

# local
from .models import Nestkast

# Reregister user
admin.site.register(Nestkast)