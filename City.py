# City contains all of the necessary information to create a general prediction
# of the weather. Latitude and longitude are retrieved via the Google Maps API
# while precipitation and average temperature are retrieved via the Weatherbit API.
# Params:
#   name:       String: Name of the city
#   lat:        Float:  Latitude of city's location
#   long:       Float:  Longitude of city's location
#   precip:     Float:  Total precipitation city has experienced in inches
#   avgTemp:    Double: Average temperature of the city within the past 10 days
class City(object):

    def __init__(self, name, lat, long, precip, avgTemp):
        self.Name = name
        self.Lat = lat
        self.Long = long
        self.Precip = precip
        self.AvgTemp = avgTemp
