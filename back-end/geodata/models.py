from django.db import models
import json
from django.utils import timezone

class Shape(models.Model):
    SHAPE_TYPES = [
        ('Star', 'Star'),
        ('Square', 'Square'),
        ('Circle', 'Circle'),
    ]

    type = models.CharField(max_length=50, choices=SHAPE_TYPES)
    coordinates = models.JSONField()
    date_created = models.DateTimeField(default=timezone.now)

    def to_json(self):
        return {
            "type": self.type,
            "coordinates": self.coordinates,
        }
