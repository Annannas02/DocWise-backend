from django.db import models
from user.models import User

class BodyMeasurements(models.Model):
    personid = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    bmi = models.IntegerField()
    timestamp = models.DateTimeField()