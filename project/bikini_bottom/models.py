# from django.db import models # Model database non spasial
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Facility(models.Model):

    TYPE_CHOICES = [
        ('government', 'Government'),
        ('public', 'Public Facility'),
        ('park', 'Park'),
        ('restaurant', 'Restaurant')
    ]

    STATUS_CHOICES = [
        ('proposed', 'Proposed'),
        ('under_review', 'Under Review'),
        ('plan', 'Plan'),
        ('cancel', 'Cancel'),
        ('construction', 'Under Construction'),
        ('completed', 'Completed')
    ]

    PRICE_CHOICES = [
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('anual', 'Anual')
    ]

    name = models.CharField(max_length=50)
    types = models.CharField(max_length=50, choices=TYPE_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='proposed')
    open = models.BooleanField(default=False)
    location = models.PointField(srid=4326, spatial_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=15, choices=PRICE_CHOICES)
    photo = models.ImageField(upload_to='facility')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)