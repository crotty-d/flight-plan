# -*- coding: utf-8 -*-
from flight_plan.airports import Airport, AirportAtlas
from flight_plan.currencies import CountryCurrencyCodes, EuroRates
from flight_plan.routes import RouteCostGraph, Itineraries


"""Main module"""

# -- Get basic airport and currency data from CSVs --

# Store airport data in AirportAtlas object
atlas = AirportAtlas(csv_filename='airport.csv')
# Store countries' currency codes CountryCurrencyCodes object
currency_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
# Store euro exchange rates for all currency codes (from euro to currency) in EuroRate object
euro_rates = EuroRates(csv_filename='currencyrates.csv')


# -- USer input --

# Request input file path from user
input_filepath = input('Please enter the full path for the itinerary CSV file to be processed: ')
# Request output filename
output_filepath = input('Please enter the path of the directory where you would like to save the calculated best routes (bestroutes.csv): ')

#TODO: For each line in input file, get itinerary (set of 5 airports) and aircraft
Itineraries(csv_filename=input_filepath)

#TODO: calculate cheapest *feasible* route