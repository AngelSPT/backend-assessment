from rest_framework import serializers
from .models import itineraries, legs, itineraries_legs

class itinerariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = itineraries
        fields = '__all__'
        
class legsSerializer(serializers.ModelSerializer):
    class Meta:
        model = legs
        fields = '__all__'

class itineraries_legsSerializer(serializers.ModelSerializer):
    class Meta:
        model = itineraries_legs
        fields = '__all__'