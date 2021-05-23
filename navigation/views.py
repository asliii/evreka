import datetime
import random

from navigation.models import *
from django.db.models import F
from django.http import JsonResponse


'''
    I filtered data by vehicle because vehicle is index on NavigationRecord. Maybe try write raw sql in orm or only raw sql.
'''
def last_points(request):
    before_48hours = datetime.datetime.now() - datetime.timedelta(hours=48)
    vehicles = list(Vehicle.objects.values_list('id', flat=True))
    points = []
    for vehicle_id in vehicles:
        data = NavigationRecord.objects.select_related('vehicle').filter(vehicle_id=vehicle_id, datetime__gte=before_48hours)
        if data.exists():
            last_data = data.order_by('-datetime').first()
            points.append({
                'vehicle_plate': last_data.vehicle.plate,
                'latitude': last_data.latitude,
                'longitude': last_data.longitude,
                'datetime': last_data.datetime.strftime('%d-%m-%Y %H:%M:%s')
            })
    return JsonResponse(points, safe=False)


def create_locations():
    for i in range(0, 10000):
        for vehicle in Vehicle.objects.all():
            loc = NavigationRecord.objects.create(
                longitude=random.uniform(32, 33),
                latitude=random.uniform(37, 39),
                vehicle=vehicle,
                datetime=(datetime.datetime.now() - datetime.timedelta(hours=random.randint(1, 100)))
            )