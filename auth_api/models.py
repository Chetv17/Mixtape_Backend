from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)