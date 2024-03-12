# sensor_api/serializers.py

from rest_framework import serializers
from .models import Sensor, SensorData
from django.shortcuts import get_object_or_404


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = SensorData
    #     fields = ['sensor', 'data', 'timestamp']

    # def create(self, validated_data):
    #     sensor_uuid = validated_data.pop('sensor', None)  # Pop the sensor field from validated_data
    #     sensor_data = {'data': validated_data['data'], 'timestamp': validated_data['timestamp']}
        
    #     if sensor_uuid:
    #         # Assuming you're using UUIDField for sensor in SensorData model
    #         sensor_data['sensor'] = sensor_uuid
        
    #     return SensorData.objects.create(**sensor_data)

    class Meta:
        model = SensorData
        fields = ['sensor', 'data', 'timestamp']

    def create(self, validated_data):
        sensor_uuid = validated_data.pop('sensor', None)
        data_value = validated_data.get('data')
        timestamp_value = validated_data.get('timestamp')

        if data_value is None:
            raise serializers.ValidationError("Data field is required.")

        if timestamp_value is None:
            raise serializers.ValidationError("Timestamp field is required.")

        sensor_data = {'data': data_value, 'timestamp': timestamp_value}

        if sensor_uuid:
            # Assuming you're using UUIDField for sensor in SensorData model
            sensor_data['sensor'] = sensor_uuid

        return SensorData.objects.create(**sensor_data)

