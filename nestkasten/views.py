# nestkasten/views.py

# django
from django.shortcuts import render
from django.views.generic.base import TemplateView


"""Markers view."""
class MarkersMapView(TemplateView):
  """Markers map view."""
  
  extra_context = {'title': 'Nestkasten'}
  template_name = "nestkasten/map.html"
