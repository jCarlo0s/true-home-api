from django.db import models


class City(models.Model):
    """ City """
    name = models.CharField(max_length=100, help_text='City name')
    
    def __str__(self):
        return self.name
