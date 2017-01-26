import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
	weather_api_key = os.environ['WEATHER_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	forecast = forecastio.load_forecast(weather_api_key, 
		location.latitude, location.longitude).currently()
	return "{} and {}°F at {}".format(forecast.summary, forecast.temperature, address)