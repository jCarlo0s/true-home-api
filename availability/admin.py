from django.contrib import admin
from .models import Availability

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = [
        'destination',
        'departure_time',
        'departure_date',
        'arrival_time',
        'arrival_date',
        'price'
        ]
    list_filter = ['departure_date', 'destination__name']

# Register your models here.
admin.site.register(Availability, AvailabilityAdmin)