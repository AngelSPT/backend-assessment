from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import itineraries, legs, itineraries_legs
from .serializers import itinerariesSerializer, legsSerializer, itineraries_legsSerializer


@api_view(['GET'])
def import_json(request):
    url = 'https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json'
    response = requests.get(url)
    data = response.json()
    data_itineraries = data['itineraries']
    data_legs = data['legs']
    
    for itineraries_data in data_itineraries:
        itinerarie = itineraries(
            id = itineraries_data['id'],
            price = itineraries_data['price'],
            agent = itineraries_data['agent'],
            agent_rating = itineraries_data['agent_rating']
        )
        
        itinerarie_legs = itineraries_data['legs']
        for itle in itinerarie_legs:
            for leg in data_legs:
                if leg['id'] == itle:
                    itin_leg = legs(
                        id = leg['id'],
                        departure_airport = leg['departure_airport'],
                        arrival_airport = leg['arrival_airport'],
                        departure_time = leg['departure_time'],
                        arrival_time = leg['arrival_time'],
                        stops = leg['stops'],
                        airline_name = leg['airline_name'],
                        airline_id = leg['airline_id'],
                        duration_mins = leg['duration_mins']
                    )
            itinerarie_leg = itineraries_legs(
                itineraries = itinerarie,
                legs = itin_leg
            )
            itinerarie_leg.save()
        
        itinerarie.save()

    for legs_data in data_legs:
        leg = legs(
            id = legs_data['id'],
            departure_airport = legs_data['departure_airport'],
            arrival_airport = legs_data['arrival_airport'],
            departure_time = legs_data['departure_time'],
            arrival_time = legs_data['arrival_time'],
            stops = legs_data['stops'],
            airline_name = legs_data['airline_name'],
            airline_id = legs_data['airline_id'],
            duration_mins = legs_data['duration_mins']
        )
        leg.save()

    return Response(data)

@api_view(['GET'])
def flights_list(request):
    itineraries_list = itineraries.objects.all()
    legs_list = legs.objects.all()
    itineraries_legs_list = itineraries_legs.objects.all()
    
    itineraries_serializer = itinerariesSerializer(itineraries_list, many=True)
    legs_serializer = legsSerializer(legs_list, many=True)
    itineraries_legs_serializer = itineraries_legsSerializer(itineraries_legs_list, many=True)
    flights_list = {}
    
    for itinerary in itineraries_serializer.data:
        for leg in itineraries_legs_serializer.data:
            if leg['itineraries'] == itinerary['id']:
                itinerary['legs'] = leg
        flights_list[itinerary['id']] = itinerary
    
    
    return Response(flights_list)