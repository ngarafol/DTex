#!/usr/bin/env python3

import pyowm
import os
import sys

# check if API_KEY env value is set

try:
    os.environ["OPENWEATHER_API_KEY"]
except KeyError:
    print ("Please set environment variable OPENWEATHER_API_KEY")
    sys.exit(1)

# check if CITY_NAME env value is set

try:
    os.environ["CITY_NAME"]
except KeyError:
    print ("Please set environment variable CITY_NAME")
    sys.exit(1)

# set env values to vars

api_key = os.environ["OPENWEATHER_API_KEY"]
city_name = os.environ["CITY_NAME"]

owm = pyowm.OWM(api_key)
weather = owm.weather_at_place(city_name)

w = weather.get_weather()

# get desired weather data

detail = w.get_detailed_status()
temp = w.get_temperature(unit='celsius')
avg = temp['temp']
humidity = w.get_humidity()

# print values as specified in exercise

print ("source=openweathermap, city="+"\""+city_name+"\""+", description="+"\""+detail+"\""+", temp="+str(avg)+", humidity="+str(humidity))
