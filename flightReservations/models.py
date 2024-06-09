from django.db import models

from flightSearch.models import Flight


# Create your models here.

class Reservation(models.Model):
    outbound = models.CharField(max_length=10)
    inbound = models.CharField(max_length=10, default=None, null=True, blank=True)
    tripType = models.CharField(max_length=10, default=None, null=True, blank=True)
    username = models.CharField(max_length=100)
