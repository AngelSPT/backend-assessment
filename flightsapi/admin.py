from django.contrib import admin
from .models import itineraries, legs, itineraries_legs

admin.site.register(itineraries)
admin.site.register(legs)
admin.site.register(itineraries_legs)