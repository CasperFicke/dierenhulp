# nestkasten/urls.py

# django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# packages
from djgeojson.views import GeoJSONLayerView

# local
from .models import Nestkast, Fourageergebied
from .views import MarkersMapView

app_name = "nestkasten"

urlpatterns = [
  path(''                                     , MarkersMapView.as_view(), name='home'),
  path('nestkasten/'                          , MarkersMapView.as_view(), name='index'),
  path('nestkasten/netkasten.geojson'         , GeoJSONLayerView.as_view(model=Nestkast,
    properties=('name', 'description', 'geom')), name='nestkasten-data'),
  
  path('nestkasten/fourageergebieden.geojson' , GeoJSONLayerView.as_view(model=Fourageergebied,
    properties=('name', 'description', 'geom')), name='fourageergebieden-data'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
