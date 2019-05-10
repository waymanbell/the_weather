#Taken from tutorial at https://scotch.io/tutorials/building-a-weather-app-in-django
#My own original contributions are an import and modification to the way the API is called

from django.shortcuts import render
import requests
from .models import City
#Added from .forms import CityForm due to error at runtime stating CityForm was undefined or declared, I don't recall which.
from .forms import CityForm


def index(request):
    cities = City.objects.all()  # return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=901ef9816be74e060e74f0eccdb1d8a1'

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:
        #Modified the next line to use city.name rather than city
        city_weather = requests.get(url.format(city.name)).json()  # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html',context)  # returns the index.html template