from django.urls import path
from healthdata import views


urlpatterns = [
    path('', views.HealthDataList.as_view()),
    path('latest', views.get_latest_health_by_username),
    path('statistics', views.get_health_by_username)
]