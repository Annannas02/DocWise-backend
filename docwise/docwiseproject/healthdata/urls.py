from django.urls import path
from healthdata import views


urlpatterns = [
    path('', views.HealthDataList.as_view()),
    path('latest', views.get_latest_health),
    path('statistics', views.get_health_statistics),
    path('addhealth/', views.add_health_data)
]