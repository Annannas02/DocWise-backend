from rest_framework import generics
from bodymeasurements import models, serializers
from rest_framework import generics

class BMList(generics.ListCreateAPIView):

    queryset = models.BodyMeasurements.objects.all()
    serializer_class = serializers.BMSerializer