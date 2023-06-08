# nestkasten/urls.py

"""Markers urls."""
# django
from django.urls import path

# local
from .views import MarkersMapView

app_name = "nestkasten"

urlpatterns = [
    path(''            , MarkersMapView.as_view(), name='home'),
    path('nestkasten/' , MarkersMapView.as_view(), name='index'),
]