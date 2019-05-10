# the_weather/weather/models.py
#Taken tutorial found at https://scotch.io/tutorials/building-a-weather-app-in-django

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def _str_(self):  # show the actual city name on the dashboard
        return self.name

    class Meta:  # show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
