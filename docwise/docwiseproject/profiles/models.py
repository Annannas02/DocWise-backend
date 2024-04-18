from django.db import models
from user.models import User

class Profile(models.Model):

    FEMALE = 1
    MALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (FEMALE, "Female"),
        (MALE, "Male"),
        (OTHER, "Other")
    )

    gender_type = models.IntegerField(choices=GENDER_TYPE)

    personid = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateTimeField()
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    img = models.CharField(max_length=50)