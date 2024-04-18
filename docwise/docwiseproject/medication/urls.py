from django.urls import path
from medication import views


urlpatterns = [
    path('', views.MedicationList.as_view())
]