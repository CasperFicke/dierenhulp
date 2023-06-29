# nestkasten/views.py

# django
from django.shortcuts import render
from django.views.generic.base import TemplateView

# local
from .models import Nestkast, Fourageergebied

"""Nestkasten view."""
class MarkersMapView(TemplateView):
  template_name = "nestkasten/All_Kasten_Gebieden.html"
    
  def get_context_data(self, **kwargs):
    title = 'Nestkasten'
    context = super().get_context_data(**kwargs)
    context['title']      = title
    context['nestkasten'] = Nestkast.objects.all()
    context['f_gebieden'] = Fourageergebied.objects.all()
    return context