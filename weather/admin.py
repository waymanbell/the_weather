#the_weather/weather/admin.py
#Taken from https://scotch.io/tutorials/building-a-weather-app-in-django

from django.contrib import admin
from .models import City

admin.site.register(City)