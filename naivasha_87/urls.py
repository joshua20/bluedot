# myapp/urls.py
from django.urls import path
from .views import raster_map

urlpatterns = [
    path('raster-map/', raster_map, name='raster_map'),
]
