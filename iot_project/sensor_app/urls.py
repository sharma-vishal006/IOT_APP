from django.urls import path
from .views import SensorListCreateView, SensorDataListCreateView,SensorDataListView,SensorDataBySensorUUIDView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensor-data/', SensorDataListCreateView.as_view(), name='sensor-data-list-create'),
    path('get-sensor-data/', SensorDataListView.as_view(), name='sensor-data-list'),
    path('sensor-data/<uuid:sensor_uuid>/', SensorDataBySensorUUIDView.as_view(), name='sensor-data-by-uuid'),
]