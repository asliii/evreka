import datetime
from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=32, verbose_name='Plate')

    def __str__(self):
        return self.plate

'''
    Exactly should be indexing by vehicle.
'''
class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Vehicle')
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    datetime = models.DateTimeField(verbose_name='Datetime', auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['vehicle', 'datetime'])]

    def __str__(self):
        return self.vehicle.plate


'''
    Should be update vehicle last location when vehicle send location. This table contains only one data per vehicle. May be use the redis is sense too.
'''
'''

class LastLocations(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Vehicle', db_index=True)
    datetime = models.DateTimeField(verbose_name='Datetime', default=datetime.datetime.now())
    location = models.ForeignKey(NavigationRecord, on_delete=models.CASCADE, verbose_name='Last Location')

    def __str__(self):
        return self.vehicle.plate + ' Last Location'

'''