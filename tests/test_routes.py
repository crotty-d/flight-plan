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


# Store airport data in AirportAtlas object
atlas = AirportAtlas(csv_filename='airport.csv')
# Store aircraft data in AircraftDictionary object
aircraft_dict = AircraftDictionary(csv_filename='aircraft.csv')
# Store countries' currency codes CountryCurrencyCodes object
currency_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
# Store euro exchange rates for all currency codes (from euro to currency) in EuroRate object
euro_rates = EuroRates(csv_filename='currencyrates.csv')


itins = Itineraries('')


# airport_atlas = AirportAtlas.load_data('input/airports.csv')
# 
# g = RouteCostGraph(airport_atlas)
# 
# cheapest_route, route_cost = Itinerary.cheapest_route(g)
