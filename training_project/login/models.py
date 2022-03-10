import email
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 120)
    email = models.EmailField(max_length= 120)
    phone_number = models.BigIntegerField(default=0)



# Create your models here.
