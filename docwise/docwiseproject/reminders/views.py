from rest_framework import generics
from reminders import models, serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Reminders
from .serializers import ReminderSerializer

class ReminderList(generics.ListCreateAPIView):

    queryset = models.Reminders.objects.all()
    serializer_class = serializers.ReminderSerializer

@api_view(['POST'])
def add_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_reminders(request):
    reminders = Reminders.objects.all()
    serializer = ReminderSerializer(reminders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reminder_by_id(request, id):
    try:
        reminder = Reminders.objects.get(id=id)
    except Reminders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ReminderSerializer(reminder)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_reminder(request, id):
    try:
        reminder = Reminders.objects.get(id=id)
    except Reminders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    reminder.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)