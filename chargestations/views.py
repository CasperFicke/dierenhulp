# chargestations/views.py

# django
from django.shortcuts import render
from django.http import JsonResponse

# python packages
from geopy.distance import geodesic

# local
from .models import EVChargingLocation, UserLocation

# index view
def index(request):
  title = 'Chargestations'
  # create a list of dictionaries(use .values) from lattitude and longgitude of the database objects
  stations = list(EVChargingLocation.objects.values('latitude', 'longitude')[:100])
  #print(stations[:2])
  context = {
    'title'   : title,
    'stations': stations
  }
  return render(request, 'chargestations/index.html', context)

# Return nearest station
def nearest_station(request):
  latitude  = request.GET.get('latitude')
  longitude = request.GET.get('longitude')
  #print(latitude, longitude)
  user_location = latitude, longitude
  station_distances = {}
  for station in EVChargingLocation.objects.all()[:100]:
    station_location = station.latitude, station.longitude
    # calculate distance
    distance = geodesic(user_location, station_location).km
    # add to list
    station_distances[distance] = station_location
  # get nearest
  min_distance = min(station_distances)
  station_coordinates = station_distances[min_distance]
  # add userlocation to db
  u_location = UserLocation(
    location_name = 'hallo',
    latitude      = latitude,
    longitude     = longitude
  )
  u_location.save()
  return JsonResponse({
     'coordinates' : station_coordinates,
     'distance'    : min_distance
  })
