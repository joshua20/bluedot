# from django.db import models
from django.contrib.gis.db import models 


# Create your models here.

class RasterData(models.Model):
    '''create a model for the RAster data'''
    name=models.CharField(max_length=100)
    raster=models.RasterField()