# mushrooms/urls.py

# django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# packages
from djgeojson.views import GeoJSONLayerView

# local
from .models import MushroomSpot
from .views import AllMushroomspotsView, ShowMushroomspotView, MushroomspotsWFSView

app_name = "mushrooms"

urlpatterns = [
  path('mushroomspots/'                   , AllMushroomspotsView.as_view(), name='index'),
  path('mushroomspots/wfs/'               , MushroomspotsWFSView.as_view(), name='wfs'),
  path('mushroomspots/data.geojson'       , GeoJSONLayerView.as_view(model=MushroomSpot,
    properties=('name', 'description', 'picture_url')), name='mushroomspots-data')
  #path('mushroomspots/<mushroomspot_id>/' , ShowMushroomspotView.as_view(), name='show_mushroomspot'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)