# the_weather/weather/urls.py
#Taken from the tutorial at https://scotch.io/tutorials/building-a-weather-app-in-django

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # the path for our index view
]
