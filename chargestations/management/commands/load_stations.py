# management/commands/load_stations.py

# gegevens uit een .csv file ophalen en opslaan in de database

# django
from django.conf import settings
from django.core.management.base import BaseCommand
from chargestations.models import EVChargingLocation

# packages
import csv

# function to import data from csv in the database
class Command(BaseCommand):
  help = 'Load data from EV Station file'

  def handle(self, *args, **kwargs):
    # location and name of the data csv
    data_file = settings.BASE_DIR / 'data' / 'Electric_Vehicle_Charging_Stations.csv'
    # the CSV columns we will gather data from.
    keys      = ('Station Name', 'New Georeferenced Column')
    
    # create empty list
    records = []
    # fill the list with desired object-items
    with open(data_file, 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      # for each row (dataobject) add dictionary with object-items named in keys
      for row in reader:
        records.append({k: row[k] for k in keys})

    # for each dataobject:
    for record in records:
      # extract the latitude and longitude from the Point object
      longitude, latitude = record['New Georeferenced Column'].split("(")[-1].split(")")[0].split()
      record['longitude'] = float(longitude)
      record['latitude']  = float(latitude)
      # and add the data to the database
      EVChargingLocation.objects.get_or_create(
        station_name = record['Station Name'],
        latitude     = record['latitude'],
        longitude    = record['longitude']
      )