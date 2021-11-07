from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, IntegerField


class User(AbstractUser):
    name = models.CharField(max_length=100)
    birth = models.DateField(default='2021-11-01')
    career = models.DateField(default='2021-11-01')
    ward = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    duty = models.JSONField(blank=True, null=True)
    is_manager = models.BooleanField(default=False)
