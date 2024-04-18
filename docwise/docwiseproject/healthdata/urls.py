from django.urls import path
from healthdata import views


urlpatterns = [
    path('', views.HealthDataList.as_view()),
    path('<str:username>/latest/', views.get_latest_health_by_username),
    path('<str:username>/', views.get_health_by_username)
]