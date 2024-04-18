from django.urls import path
from healthdata import views


urlpatterns = [
    path('', views.HealthDataList.as_view())
]