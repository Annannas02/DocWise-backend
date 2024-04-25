from rest_framework import generics
from medication import models, serializers
from reminders.models import Reminders
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone

class MedicationList(generics.ListCreateAPIView):

    queryset = models.Medication.objects.all()
    serializer_class = serializers.MedicationSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_medication(request):
    user = request.user

    name = request.data.get("name")
    medication_type = request.data.get("medication_type")
    strength = request.data.get("strength")
    unit_type = request.data.get("unit_type")
    notes = request.data.get("notes")

    next_reminder = request.data.get("next_reminder")

    if medication_type >=1  and medication_type <= 5 and unit_type >= 1 and unit_type <= 5:
        medication = models.Medication.objects.create(
            personid=user,
            name=name,
            medication_type=medication_type,
            strength=strength,
            unit_type=unit_type,
            notes=notes
        )
        
        reminder = Reminders.objects.create(
            medicationid=medication,
            next_reminder=next_reminder
        )
        serialized_medication = serializers.MedicationSerializer(medication)
        return Response(serialized_medication.data,status=status.HTTP_201_CREATED)

    else:
        return Response("Invalid data params",status=status.HTTP_400_BAD_REQUEST)
    
    