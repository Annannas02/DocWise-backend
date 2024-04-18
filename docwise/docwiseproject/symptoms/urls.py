from django.urls import path
from symptoms import views


urlpatterns = [
    path('', views.SymptomsList.as_view())
]