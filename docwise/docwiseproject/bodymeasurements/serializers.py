from rest_framework import serializers
from bodymeasurements import models

class BMSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BodyMeasurements
        fields = '__all__'