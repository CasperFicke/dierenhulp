# chargestations/urls.py

"""Chargestations urls."""
# django
from django.urls import path
from . import views

# local
#from .views import 

app_name = "chargestations"

urlpatterns = [
  path('chargestations/'                     , views.index, name= 'index'),
  path('chargestations/get-nearest-station'  , views.nearest_station, name= 'nearest-station'),
]