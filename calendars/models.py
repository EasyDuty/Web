from django.db import models
from django.conf import settings


class ApplyOff(models.Model):
    day = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)