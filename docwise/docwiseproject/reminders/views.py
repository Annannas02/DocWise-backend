from rest_framework import generics
from reminders import models, serializers
from rest_framework import generics

class ReminderList(generics.ListCreateAPIView):

    queryset = models.Reminders.objects.all()
    serializer_class = serializers.ReminderSerializer