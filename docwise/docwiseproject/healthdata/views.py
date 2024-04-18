from rest_framework import generics
from healthdata import models, serializers
from rest_framework import generics

class HealthDataList(generics.ListCreateAPIView):

    queryset = models.HealthData.objects.all()
    serializer_class = serializers.HealthDataSerializer