# mushroomspots/views.py


# django
from django.shortcuts import render
from django.views.generic.base import TemplateView

# packages
from gisserver.features import FeatureType, ServiceDescription
from gisserver.geometries import CRS, WGS84
from gisserver.views import WFSView

# local
from .models import MushroomSpot

RD_NEW = CRS.from_srid(28992)
WGS_84 = CRS.from_srid(4326)

# All Mushroomspots view
class AllMushroomspotsView(TemplateView):
  template_name = "mushrooms/all_mushroomspots.html"
 
  def get_context_data(self, **kwargs):
    title = 'Mushroomspots'
    context = super().get_context_data(**kwargs)
    context['title']      = title
    context['qs_results'] = MushroomSpot.objects.all()
    return context

# Show Mushroomspot view
class ShowMushroomspotView(TemplateView):
  template_name = "mushrooms/show_mushroomspot.html"

  def get_context_data(self, **kwargs):
    title = 'Mushroomspot'
    context = super().get_context_data(**kwargs)
    context['title']        = title
    context['mushroomspot'] = MushroomSpot.objects.all()
    return context

# Mushroomspots WFS
class MushroomspotsWFSView(WFSView):
  xml_namespace = "http://example.org/gisserver"

  # The service metadata
  service_description = ServiceDescription(
    title          = "Mushroomspots",
    abstract       = "Unittesting",
    keywords       = ["django-gisserver"],
    provider_name  = "Datalab",
    provider_site  = "https://purmerend.nl/in-purmerend-en-beemster/datalab-purmerend",
    contact_person = "datalab Purmerend",
  )

  # Each Django model is listed here as a feature.
  feature_types = [
    FeatureType(
      MushroomSpot.objects.all(),
      fields    = "__all__",
      other_crs = [RD_NEW]
    ),
  ]