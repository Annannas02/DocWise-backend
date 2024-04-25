from rest_framework import serializers
from medication import models
from reminders.models import Reminders

class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Medication
        fields = '__all__'
    
