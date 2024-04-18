from rest_framework import generics
from symptoms import models, serializers
from rest_framework import generics

class SymptomsList(generics.ListCreateAPIView):

    queryset = models.Symptoms.objects.all()
    serializer_class = serializers.SymptomSerializer