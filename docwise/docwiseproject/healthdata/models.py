from django.db import models
from user.models import User

class HealthData(models.Model):
    personid = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.FloatField()
    pulse = models.IntegerField()
    oxygen = models.IntegerField()
    timestamp = models.DateTimeField()