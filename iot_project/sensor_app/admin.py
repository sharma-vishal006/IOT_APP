from django.contrib import admin

# sensor_api/admin.py
from .models import Sensor, SensorData

admin.site.register(Sensor)
admin.site.register(SensorData)
