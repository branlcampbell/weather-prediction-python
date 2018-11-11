# Class for making Weatherbit API calls. This class will be instantiated as a
# singleton to gather all necessary information from the API.
from weatherbit.api import Api
import API_Key
import json

# Get the private key string from API_KEY.
api_key = API_Key.API_Key().Weatherbit_Key

# Authenticate our API Key. This variable will be used for all API calls.
weatherbit = Api(api_key)

# Set the API for retrieving the daily forecast.
weatherbit.set_granularity('daily')

# Gets the forecast for the current day.
# Params:
#   lat:    Float: The latitude of the city.
#   long:   Float: The longitude of the city.
# Return: List containing the precipitation, average temperature, and max
# temperature per hour from midnight to the current hour.
def get_daily_forecast(lat, long):
    forecast = weatherbit.get_forecast(lat = lat, lon = long)
    precip = forecast.json['data'][0]['precip']
    precip = precip / 25.4 # Convert mm to inches
    avg_temp = forecast.json['data'][0]['temp']
    avg_temp = avg_temp * 1.8 + 32 # Convert Celsius to Fahrenheit
    max_temp = forecast.json['data'][0]['max_temp']
    max_temp = max_temp * 1.8 + 32
    weather = [precip, avg_temp, max_temp]
    return weather

# Gets the forecast for a day that has already passed.
# Params:
#   lat:    Float:  The latitude of the city.
#   long:   Float:  The longitude of the city.
#   start_date: String: The date to be searched in format YYYY-MM-DD.
#   end_date:   String: The end of the date range to be searched.
# Return: List containing the precipation, average temperature, and max
# temperature for the specified day.
# Note: Given the API limits, only one day can be queried at a time. The free
# tier of the Weatherbit API appears to also limit data to the current year.
def get_previous_forecast(lat, long, start_date, end_date):
    history = weatherbit.get_history(lat = lat, lon = long, start_date = start_date, end_date = end_date)
    precip = history.json['data'][0]['precip']
    # For some reason, certain cities did not return precipitation data from their API call.
    # To account for this, JSON that returns 'None' will instead return 0.0
    if(precip == None):
        precip = 0.0
    avg_temp = history.json['data'][0]['temp']
    avg_temp = avg_temp * 1.8 + 32 # Convert to Fahrenheit
    max_temp = history.json['data'][0]['max_temp']
    max_temp = max_temp * 1.8 + 32
    weather = [precip, avg_temp, max_temp]
    return weather
