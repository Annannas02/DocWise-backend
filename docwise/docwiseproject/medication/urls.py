from django.urls import path
from medication import views


urlpatterns = [
    path('', views.MedicationList.as_view()),
    path('add-medication/', views.add_medication)
]