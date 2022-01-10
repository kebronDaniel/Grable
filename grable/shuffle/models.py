import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.utils import timezone


class Round(models.Model):
    name = models.CharField(max_length=255)
    members = models.TextField(default="")
    location = models.TextField(default="")
    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class StaffProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    isAvailable = models.BooleanField(default=True)
    firstDegree = models.CharField(max_length=100)
    secondDegree = models.CharField(max_length=100)
    perviousOccupation = models.CharField(max_length=100, null=True)
    recruitmentYear = models.DateField(default=datetime.date.today)
    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Location(models.Model):
    name = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
