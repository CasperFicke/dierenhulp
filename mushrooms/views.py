from django.shortcuts import render

from django.views.generic.base import TemplateView

# local
from .models import MushroomSpot

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

