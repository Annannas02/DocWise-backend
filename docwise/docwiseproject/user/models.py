from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    password = models.CharField( null=False)

    #last_login = models.DateField()
    #is_staff = models.BooleanField(default=False)

    USERNAME_FIELD='username'