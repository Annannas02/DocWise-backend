from django.urls import path
from reminders import views

urlpatterns = [
    path('', views.ReminderList.as_view()),
    path('add', views.add_reminder),
    path('get', views.get_reminders),
    path('get/<int:id>', views.get_reminder_by_id),
    path('delete/<int:id>', views.delete_reminder)
]