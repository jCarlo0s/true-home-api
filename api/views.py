from django.shortcuts import render
from rest_framework import viewsets
from cities.models import City
from availability.models import Availability
from .serializers import CitySerializer, AvailabilitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """ Api for cities """
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer


class AvailabilityViewSet(viewsets.ReadOnlyModelViewSet):
    """ Api to retrive the availability from city """
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

    def get_queryset(self):
        destination_pk = self.request.query_params.get('destination', None)
        try:
            if destination_pk:
                return self.queryset.filter(destination=int(destination_pk))
        except ValueError as error:
            return super().get_queryset()
    
    
