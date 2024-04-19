from rest_framework import serializers
from healthdata import models

class HealthDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HealthData
        exclude = ('id', 'personid')