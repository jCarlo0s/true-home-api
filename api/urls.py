from django.urls import include, path
from rest_framework import routers
from .views import CityViewSet, AvailabilityViewSet

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'availability', AvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls))
]