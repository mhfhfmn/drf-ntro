from django.urls import path
from .views import MeasurementViewCreate, SensorView, MeasurementView, SensorViewUpdate

urlpatterns = [
    path('sensors/', SensorView.as_view(), name="smart_home"),
    path('sensors/<int:pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurements/<int:pk>/', MeasurementViewCreate.as_view())
]
