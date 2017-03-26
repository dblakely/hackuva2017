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

    category = models.CharField(max_length=300, null=True)

    def to_dict(self):
        return {
            'name': self.name,
            'location_name': self.location_name,
            'datetime': self.datetime.isoformat(),
            'latitude': float(self.latitude),
            'longitude': float(self.longitude),
            'category': self.category or 'None',
        }
