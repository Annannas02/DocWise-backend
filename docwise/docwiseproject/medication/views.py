from rest_framework import generics
from medication import models, serializers
from rest_framework import generics

class MedicationList(generics.ListCreateAPIView):

    queryset = models.Medication.objects.all()
    serializer_class = serializers.MedicationSerializer