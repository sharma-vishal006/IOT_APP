from django.shortcuts import render

# Create your views here.
# sensor_api/views.py

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from .models import Sensor, SensorData
from .serializers import SensorSerializer, SensorDataSerializer
from django.core.exceptions import ValidationError


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_sensors = self.request.user.sensors.all()  # This assumes each user can have multiple sensors
        if not user_sensors.exists():
            raise ValidationError("This user does not have any sensors.")
        # Assuming you want to use the first sensor or a specific sensor determined by some logic
        serializer.save(sensor=user_sensors.first())


class SensorDataListView(generics.ListAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer



class SensorDataBySensorUUIDView(generics.ListAPIView):
    serializer_class = SensorDataSerializer

    def get_queryset(self):
        sensor_uuid = self.kwargs['sensor_uuid']
        sensor_data = SensorData.objects.filter(sensor=sensor_uuid)
        return sensor_data