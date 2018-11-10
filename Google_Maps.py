# Class for making Google Geocoding API calls. This class will be instantiated as a
# singleton to gather all necessary information from the API.
import googlemaps
import API_Key

# Get the private key string from API_KEY.
api_key = API_Key.API_Key().Google_Key

gmaps = googlemaps.Client(key = api_key)

# Geocoding an address
geocode_result = gmaps.geocode('New York City, NY')

print geocode_result
