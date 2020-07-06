from django.db import models
from django.contrib.gis.db import models as geomodels

# City Table in PostgresSQL storing co-ordinates and geo-data
class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    geometry = geomodels.PointField()
    temperature = models.FloatField(default=10.1)

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'cities'
