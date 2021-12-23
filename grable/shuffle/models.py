from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.utils import timezone


class Round(models.Model):
    name = models.CharField(max_length=255)
    members = models.TextField(default="")
    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
