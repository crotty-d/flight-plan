#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for routes module."""

import pytest
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
csv_filepath = '/home/d/Git/flight_plan/flight_plan/input/input.csv'

#-- Itinerary tests --
itins = Itineraries(csv_filepath, atlas, aircraft_dict)
for route in itins.best_routes():
    print(route)


