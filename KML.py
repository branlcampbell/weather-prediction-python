# Responsible for creating a KML file using data from all API calls.
import simplekml
import sys
import os

# Generates the KML file from the attributes in each City object.
# Each city object is represented as a placemark placed where the city's
# center latitude and longitude are located. The KML file created is saved
# in the program's working directory.
# Params:
#   city_objects_list:  List:   A list of all City objects created.
def generate_kml_file(city_objects_list):
    print "Generating KML file..."
    kml = simplekml.Kml()
    for cities in city_objects_list:
        kml.newpoint(name = cities.Name,
        description = "Average temperature: " + str(cities.AvgTemp) + "\n"
        "Average precipitation: " + str(cities.Precip) + "\n"
        "Average precipitation per hour: " + str(cities.Precip / 24) + "\n",
        coords = [(cities.Long, cities.Lat)])
    try:
        kml.save("Data.kml")
        print "Done"
        print "Data.KML is saved in " + os.getcwd()
    except:
        e = sys.exc_info()[0]
        print e
