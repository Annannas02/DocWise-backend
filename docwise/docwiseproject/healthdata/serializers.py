from rest_framework import serializers
from healthdata import models
from django.utils import timezone
from user.models import User

class HealthDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HealthData
        exclude = ('id', 'personid')
