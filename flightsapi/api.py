from .models import itineraries, legs, itineraries_legs
from rest_framework import viewsets, permissions    
from .serializers import itinerariesSerializer, legsSerializer, itineraries_legsSerializer

class itinerariesViewSet(viewsets.ModelViewSet):
    queryset = itineraries.objects.all()
    serializer_class = itinerariesSerializer
    permission_classes = [permissions.AllowAny]

class legsViewSet(viewsets.ModelViewSet):
    queryset = legs.objects.all()
    serializer_class = legsSerializer
    permission_classes = [permissions.AllowAny]

class itineraries_legsViewSet(viewsets.ModelViewSet):
    queryset = itineraries_legs.objects.all()
    serializer_class = itineraries_legsSerializer
    permission_classes = [permissions.AllowAny]