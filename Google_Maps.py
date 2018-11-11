# Class for making Google Geocoding API calls. This class will be instantiated as a
# singleton to gather all necessary information from the API.
import googlemaps
import API_Key
import json
import urllib

# Get the private key string from API_KEY.
api = API_Key.API_Key().Google_Key

# Gets geocode coordinates for the specified city by making a urllib request
# through the string generated. The JSON response is then converted and parsed
# for the necessary information.
# Params:
#   city: String: The name of the city to be geocoded.
# Return: List containing the city's name, latitude, and longitude.
def get_geocode(city):

    base = r"https://maps.googleapis.com/maps/api/geocode/json?"
    addP = "address=" + city.replace(" ","+")
    GeoUrl = base + addP + "&key=" + api
    response = urllib.urlopen(GeoUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)

    if jsonData['status'] == 'OK':
        results = jsonData['results'][0]
        finList = [results['formatted_address'],results['geometry']['location']['lat'],results['geometry']['location']['lng']]
    else:
        finList = [None,None,None]

    return finList
