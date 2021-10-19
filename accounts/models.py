from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, IntegerField


class User(AbstractUser):
    name = CharField(max_length=100)
    age = IntegerField()
    career = IntegerField()
    ward = CharField(max_length=100)
    team = CharField(max_length=100)
    hospital = CharField(max_length=100)
    duty = CharField(blank=True, max_length=31)
    
