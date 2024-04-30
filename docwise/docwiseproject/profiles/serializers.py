from rest_framework import serializers
from profiles import models
from user import serializers as users_serializers

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = '__all__'