from django.db import models
from cities.models import City

# Create your models here.
class Availability(models.Model):
    """ Availability model """
    destination = models.ForeignKey(City, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    departure_date = models.DateField()
    arrival_date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.destination.name