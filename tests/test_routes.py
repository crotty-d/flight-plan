#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for routes module."""

import pytest
import os
import sys
sys.path.append('.')

from flight_plan.airports import AirportAtlas
from flight_plan.aircraft import AircraftDictionary
from flight_plan.currencies import CountryCurrencyCodes, EuroRates
from flight_plan.routes import RouteGraph, Itineraries

# -- Data --
# Currency data
currency_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
euro_rates = EuroRates(csv_filename='currencyrates.csv')
# Airport data
atlas = AirportAtlas('airport.csv', currency_codes, euro_rates)
# Aircraft data
aircraft_dict = AircraftDictionary(csv_filename='aircraft.csv')
# Testroutes
csv_filepath = '/home/d/Git/flight_plan/flight_plan/input/testroutes.csv'

#-- Itinerary tests --
def test_best_routes():
    true_best = [['DUB', 'LHR', 'AAL', 'SYD', 'JFK', 'DUB', '777', 20349.645364201853],
['SNN', 'ORK', 'CDG', 'SIN', 'MAN', 'SNN', 'A330', 19775.81003691762],
['BOS', 'ORD', 'SFO', 'DFW', 'ATL', 'BOS', '737', 8921.617540737174],
['DUB', 'CDG', 'AAL', 'OSL', 'SVO', 'DUB', 'A330', 2080.7972240233103]]
    
    assert Itineraries(csv_filepath, atlas, aircraft_dict).best_routes() == true_best

    
def test_to_csv():
    itins = Itineraries(csv_filepath, atlas, aircraft_dict)
    itins.best_routes()
    itins.routes_to_csv()
    actual_files = os.listdir('/home/d/Git/flight_plan/flight_plan/output')
    required_file = 'bestroutes.csv'
    assert required_file in actual_files
    



