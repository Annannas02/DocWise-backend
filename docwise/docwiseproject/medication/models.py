from django.db import models
from user.models import User

class Medication(models.Model):
    
    CAPSULE = 1
    TABLET = 2
    LIQUID = 3
    LOTION = 4
    INJECTION = 4
    OTHER = 5
    MEDICATION_TYPE = (
        (CAPSULE, "Capsule"),
        (TABLET, "Tablet"),
        (LIQUID, "Liquid"),
        (LOTION, "Lotion, gel, foam, cream"),
        (INJECTION, "Injection"),
        (OTHER, "Other")
    )

    MG = 1
    MCG = 2
    G = 3
    ML = 4
    PERCENT = 5
    UNIT_TYPE = {
        (MG, "mg"),
        (MCG, "mcg"),
        (G, "g"),
        (ML, "mL"),
        (PERCENT, "%")
    }

    personid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    medication_type = models.PositiveIntegerField(choices=MEDICATION_TYPE)
    strength = models.PositiveIntegerField()
    unit_type = models.PositiveIntegerField(choices=UNIT_TYPE)
    notes = models.CharField(max_length=500)
    