from cities.models import City
from availability.models import Availability
from rest_framework import serializers

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['pk', 'name']


class AvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Availability
        fields = ['pk', 'destination', 'departure_time', 'departure_date', 'arrival_time', 'arrival_date', 'price']