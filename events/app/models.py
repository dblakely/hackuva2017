from django.db import models


class Event(models.Model):
    """
    Represents a single event.
    """
    name = models.CharField(max_length=300)
    location_name = models.CharField(max_length=300)
    datetime = models.DateTimeField()
    latitude = models.DecimalField(max_digits=50, decimal_places=20)
    longitude = models.DecimalField(max_digits=50, decimal_places=20)

