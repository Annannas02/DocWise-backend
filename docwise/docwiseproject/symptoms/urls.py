from django.urls import path
from symptoms import views


urlpatterns = [
    path('', views.SymptomsList.as_view()),
    path('get', views.get_user_symptoms),
    path('add/', views.add_symptom)
]