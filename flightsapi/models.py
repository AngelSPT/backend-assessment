from django.db import models

# Model itineraries - These are the containers for your trips, 
# tying together Legs, and prices. Prices are offered by an agent 
# - an airline or travel agent.
class itineraries(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    price = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    agent_rating = models.DecimalField(max_digits=10, decimal_places=2)


# Model Legs - These are journeys (outbound, return) with duration, stops and airlines.
class legs(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    airline_name = models.CharField(max_length=100)
    airline_id = models.CharField(max_length=100)
    duration_mins = models.IntegerField()


# Model itineraries_legs - Relationship between itineraries and legs
class itineraries_legs(models.Model):
    itineraries = models.ForeignKey(itineraries, on_delete=models.CASCADE)
    legs = models.ForeignKey(legs, on_delete=models.CASCADE)