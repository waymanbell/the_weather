#the_weather/weather/forms.py
#Taken from tutorial at https://scotch.io/tutorials/building-a-weather-app-in-django

from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'cityname': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder