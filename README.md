# Weather Prediction - Python

This program utilizes the Google Geocoding API and Weatherbit.io API to gather weather data for major US cities. An average for each portion of a city's weather data is found and all data is saved in a City object. Once all objects are created, a KML file is generated using simpleKML. This KML file contains points on the map at the location of each city. These points contain the data gathered and can potentially be used to analyze weather patterns in areas and predict if a drought or flood may occur.

![](/Screenshot.png)

## Getting Started

These instructions will provide a step-by-step guide on how to run the scripts and make the required API calls.

### Prerequisites

#### Software

This program requires python 2.x to run. Please follow the installation instructions for your system on https://www.python.org/

#### API Keys

In order to retrieve the required JSON data, you must have API keys registered with Weatherbit.io and Google Cloud Platform. Please visit https://www.weatherbit.io/ and https://developers.google.com/ to sign up and register for your own API keys. The Weatherbit.io free tier is acceptable for the current scope of this project. When generating a Google Cloud Platform API Key, only the Geocoding service is required to make the appropriate Google API calls.

#### Package Dependencies

The following packages are required in order to run this program:
* simpleKML
* pyweatherbit

To install, enter the following commands through your terminal:

```
pip install simplekml
```

```
pip install pyweatherbit
```

### Installing

To install, clone this respository and fulfill the above prerequisites. Upon cloning, you must create a new python file called API_Key.py. This file is a container for your API keys for source control. Paste the following into API_KEY.py with the API Keys inserted where appropriate.

```
class API_Key(object):
    def __init__(self):
        self.Weatherbit_Key = "WEATHERBIT API KEY"
        self.Google_Key = "GOOGLE API KEY"
```

Once this file is created, you can run the program. First, change your directory to the location of the cloned repository, then run Main through terminal.

```
cd /path/to/weather-prediction-python
python Main.py
```

## Utilizing Generated KML Data

Once the program has finished its execution, you will see that a file named Data.KML has been created within the current working directory of the program. To view its contents on a map, visit Google My Maps and create a new map through the dashboard. Once a map has been created, a KML layer can be imported onto the map. Click the import button and navigate to Data.KML and import the file. Once importing has completed, all points on the map should be displayed. Click on any of these points for more information on them.

## Bugs / Issues

To notify of any bugs / issues running this script, please contact me with all errors printed to the console.


## Built With

* [Python](http://python.org/) - Language used.
* [Weatherbit.io](https://www.weatherbit.io/api) - API for weather data.
* [Google Cloud Platform](https://cloud.google.com/maps-platform/) - API for geocoding cities.
* [weatherbit-python](https://github.com/weatherbit/weatherbit-python) - Python wrapper for Weatherbit API calls.

## Authors

* **Brandon Campbell**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Weatherbit.IO
* Google Cloud Platform
* simpleKML developers
