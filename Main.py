# This program utilizes the Google Geocoding API and Weatherbit.io API to
# gather weather data for major US cities. An average for each portion
# of a city's weather data is found and all data is saved in a City object.
# Once all objects are created, a KML file is generated using pyKML. This
# KML file contains points on the map at the location of each city. These
# points contain the data gathered and are color-coded to determine whether
# or not there is the possibility of any natural disasters/hazards, such as
# droughts or flooding.
import Google_Maps as google
import Weatherbit as weatherbit
import City
import datetime
from calendar import monthrange

#citiesList = ["New York, NY", "Boston, MA", "Philadelphia, PA",
#"Chicago, IL", "Denver, CO", "Seattle, WA", "Los Angeles, CA",
#"Houston, TX", "Las Vegas, NV", "Miami, FL"]

date = datetime.datetime.now()

cities_list = ["New York, NY"]

city_objects_list = []

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
    while(i < 1):
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
        total_precip = total_precip + weather[0]
        total_avg_temp = total_avg_temp + weather[1]
        i = i + 1

    # Find the average for precipitation and temperature for all days in the data.
    total_precip = total_precip / 10
    total_avg_temp = total_avg_temp / 10
    # Create the City object using the gathered data and store it in a list.
    City = City.City(geocoding[0], geocoding[1], geocoding[2], total_precip, total_avg_temp)
    city_objects_list.append(City)
