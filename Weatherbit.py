# Class for making Weatherbit API calls. This class will be instantiated as a
# singleton to gather all necessary information from the API.
from weatherbit.api import Api
import API_Key
import json

# Get the private key string from API_KEY.
api_key = API_Key.API_Key().Weatherbit_Key

# Authenticate our API Key. This variable will be used for all API calls.
weatherbit = Api(api_key)

# Set the API for retreving the daily forecast.
weatherbit.set_granularity('daily')

lat = 40.730610
long = 	-73.935242

history = weatherbit.get_history(lat=lat, lon=long, start_date='2018-11-09',end_date='2018-11-10')
forecast = weatherbit.get_forecast(lat = lat, lon = long)

data = history.get_series(['precip', 'max_temp'])

for row in data:
    print(row)

#with open('data.json', 'w') as outfile:
#    json.dump(data, outfile)
