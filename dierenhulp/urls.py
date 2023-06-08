# dierenhulp/urls.py

"""mymap URL Configuration."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('nestkasten.urls', namespace='nestkasten')),
  path('', include('chargestations.urls', namespace='chargestations')),
]
