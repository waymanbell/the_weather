#the_weather/the_weather/urls.py
#Taken from https://scotch.io/tutorials/building-a-weather-app-in-django

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
]