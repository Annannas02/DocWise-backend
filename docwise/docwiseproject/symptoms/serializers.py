from rest_framework import serializers
from symptoms import models

class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Symptoms
        fields = '__all__'