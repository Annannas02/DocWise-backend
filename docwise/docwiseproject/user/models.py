from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(max_length=50,unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=30,null=False)
    secret = models.CharField(max_length=17, null=True)

    USERNAME_FIELD='username'