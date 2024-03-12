from django.db import models
import uuid
from django.conf import settings

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        ordering = ["-created_at"]
        
# sensor_api/models.py
class Sensor(BaseModel):
    SENSOR_TYPES = (
        ('ENV', 'Environmental'),
        ('ELECTRICAL', 'Electrical'),
        ('TEMPERATURE', 'Temperature'),
        ('PRESSURE','Pressure'),
        ('SMOKE','Smoke'),
        ('ALCOHOL','Alcohol')
        # Add more sensor types as needed
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sensors', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sensor_type = models.CharField(max_length=11, choices=SENSOR_TYPES)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.get_sensor_type_display()} Sensor: {self.name} in {self.location}"

class SensorData(BaseModel):
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    data = models.JSONField()  # Storing data as JSON for flexibility

    def __str__(self):
        return f"Data from {self.sensor.name} at {self.timestamp}"
