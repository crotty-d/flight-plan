# -*- coding: utf-8 -*-

from airports import AirportAtlas
from aircraft import AircraftDictionary
from currencies import CountryCurrencyCodes, EuroRates
from routes import Itineraries


"""Main module"""

# -- Get basic airport and currency data from CSVs --

# Store countries' currency codes CountryCurrencyCodes object
currency_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
# Store euro exchange rates for all currency codes (from euro to currency) in EuroRate object
euro_rates = EuroRates(csv_filename='currencyrates.csv')
# Store airport data in AirportAtlas object
atlas = AirportAtlas('airport.csv', currency_codes, euro_rates)
# Store aircraft data in AircraftDictionary object
aircraft_dict = AircraftDictionary(csv_filename='aircraft.csv')


# -- User input --

# Request input file path from user
input_filepath = input('Please enter the full path for the itinerary CSV file to be processed: ')
# Request output filename
output_filepath = input('Please enter the path of the directory where you would like to save the calculated best routes (bestroutes.csv): ')

# Get best routes
if output_filepath is not None:
    itins = Itineraries(input_filepath, atlas, aircraft_dict, outut_csv_path=output_filepath)
else:
    itins = Itineraries(input_filepath, atlas, aircraft_dict) # use default path (output folder)

itins.best_routes()

# Save output to CSV
itins.routes_to_csv()