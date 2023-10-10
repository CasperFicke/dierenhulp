# dierenhulp/urls.py

"""mymap URL Configuration."""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('nestkasten.urls', namespace='nestkasten')),
  path('', include('chargestations.urls', namespace='chargestations')),
  path('', include('mushrooms.urls', namespace='mushrooms')),
]

if settings.DEBUG: # DEVELOPMENT ONLY
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # url compositie voor externe toegang tot staticfiles
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # url compositie voor externe toegang tot mediafiles

