# This program utilizes the Google Geocoding API and Weatherbit.io API to
# gather weather data for major US cities. An average for each portion
# of a city's weather data is found and all data is saved in a City object.
# Once all objects are created, a KML file is generated using simpleKML. This
# KML file contains points on the map at the location of each city. These
# points contain the data gathered and can potentially be used to analyze
# weather patterns in areas and predict if a drought or flood may occur.
import Google_Maps as google
import Weatherbit as weatherbit
import KML as kml
import City as city
import datetime
from calendar import monthrange

# Hardcoded list of cities to gather information for. This can be replaced
# in the future with external data.
cities_list = ["New York, NY", "Boston, MA", "Philadelphia, PA",
"Chicago, IL", "Denver, CO", "Seattle, WA", "Los Angeles, CA",
"Houston, TX", "Las Vegas, NV", "Miami, FL"]
city_objects_list = []
date = datetime.datetime.now()

for cities in cities_list:
    print "Retrieving weather information for " + cities + "..."
    day = date.day
    month = date.month
    year = date.year
    geocoding = google.get_geocode(cities)
    lat = geocoding[1]
    long = geocoding[2]
    total_precip = 0.0
    total_avg_temp = 0.0

    # This formats a string representing the date and gets the previous n
    # amount of days. This loop accounts of having to go back to the previous
    # month / year and will adjust accordingly.
    i = 0
    max = 1 # Placeholder in case user input is implemented.
    while(i < max):
        currentDate = str(year) + "-" + str(month) + "-" + str(day)
        day = day - 1
        # Out of calendar range, so the last day of the previous month must be found.
        if(day < 1):
            month = month - 1
            # Month can just be set to December. We already know the calendar month range.
            # Year is also just decremented by 1.
            if(month < 1):
                month = 12
                year = year - 1
            # monthrange returns a tuple, so we want the upper bound returned.
            day = monthrange(year, month)[1]
        previousDate = str(year) + "-" + str(month) + "-" + str(day)
        weather = weatherbit.get_previous_forecast(lat, long, previousDate, currentDate)
        #print weather
        total_precip = total_precip + weather[0]
        total_avg_temp = total_avg_temp + weather[1]
        i = i + 1

    # Find the average for precipitation and temperature for all days in the data.
    total_precip = total_precip / max
    total_avg_temp = total_avg_temp / max
    # Create the City object using the gathered data and store it in a list.
    City = city.City(geocoding[0], geocoding[1], geocoding[2], total_precip, total_avg_temp)
    city_objects_list.append(City)

kml.generate_kml_file(city_objects_list)
