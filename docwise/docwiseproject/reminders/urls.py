from django.urls import path
from reminders import views

urlpatterns = [
    path('', views.ReminderList.as_view())
]