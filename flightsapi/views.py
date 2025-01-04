from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import itineraries, legs, itineraries_legs


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
        
        #itinerarie_legs = itineraries_data['legs']
        #for itle in itinerarie_legs:
        #    itinerarie_leg = itineraries_legs(
        #        itineraries = itinerarie,
        #        legs = itle
        #    )
        #itinerarie_leg.save()
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