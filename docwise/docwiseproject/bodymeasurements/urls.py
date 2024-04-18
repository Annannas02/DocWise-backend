from django.urls import path
from bodymeasurements import views


urlpatterns = [
    path('', views.BMList.as_view())
]