from rest_framework import routers
from django.urls import path, include, re_path
from .api import itinerariesViewSet, legsViewSet, itineraries_legsViewSet
from .views import import_json, flights_list

router = routers.DefaultRouter()

router.register('api/itineraries', itinerariesViewSet, 'itineraries')
router.register('api/legs', legsViewSet, 'legs')
router.register('api/itinerarieslegs', itineraries_legsViewSet, 'itinerarieslegs')

urlpatterns = router.urls


urlpatterns += [
    re_path('api/import', import_json, name='import_json'),
    re_path('api/flights/list', flights_list, name='flights_list'),
    
]
