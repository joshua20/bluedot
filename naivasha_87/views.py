# myapp/views.py
from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Transform
from .models import RasterData


# Create your views here.
def raster_map(request):
    # Center coordinates (longitude, latitude)
    center_point = Point(x=0.7754, y=36.3715, srid=4326)

    # Transform the point to the coordinate system of the raster data
    transformed_point = center_point.transform(4326)

    # Query the raster data for the transformed point
    raster_data = RasterData.objects.filter(raster__covers=transformed_point).first()

    return render(request, 'naivasha_87/raster_map.html', {'raster_data': raster_data})
