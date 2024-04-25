from django.db import models
from medication.models import Medication

class Reminders(models.Model):
    medicationid = models.ForeignKey(Medication, on_delete=models.CASCADE)
    next_reminder = models.DateTimeField()
    reminder_displayed = models.BooleanField(default=False)