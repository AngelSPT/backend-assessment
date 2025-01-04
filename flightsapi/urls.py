from rest_framework import routers
from django.urls import path, include
from .api import itinerariesViewSet, legsViewSet, itineraries_legsViewSet

router = routers.DefaultRouter()

router.register('api/itineraries', itinerariesViewSet, 'itineraries')
router.register('api/legs', legsViewSet, 'legs')
router.register('api/itinerarieslegs', itineraries_legsViewSet, 'itinerarieslegs')

urlpatterns = router.urls