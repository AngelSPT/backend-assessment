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

    #for itineraries_data in data:
    #    itinerarie = itineraries(
    #        id = itineraries_data['id'],
    #        price = itineraries_data['price'],
    #        agent = itineraries_data['agent'],
    #        agent_rating = itineraries_data['agent_rating']
    #    )
    #    itinerarie.save()

    return Response(data)