#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for airports module."""

import pytest
import sys
sys.path.append('.')

from flight_plan.airports import Airport, AirportAtlas
from flight_plan.currencies import CountryCurrencyCodes, EuroRates

# -- Airport -- 
def test_Aiport():
    # Create airport instance
    params = ('DUB', 'Dublin', 'Ireland', 51.841269, -8.491111)
    airport = Airport(*params)
    
    # Check methods return correct value
    assert airport.get_code() == params[0]
    assert airport.get_city() == params[1]
    assert airport.get_country() == params[2]
    assert airport.get_latitude() == params[3]
    assert airport.get_longitude() == params[4]
    
# -- AirportAtlas --
# def test_construct_default_AirportAtlas():
#     atlas = AirportAtlas()
#     assert atlas.get_dict() == {}

# Create airport atlas from CSV for use in tests below, and check dict is not empty
## First, create instances of currency information objects for use in airport atlas
currency_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
euro_rates = EuroRates(csv_filename='currencyrates.csv')
csv_atlas = AirportAtlas('airport.csv', currency_codes, euro_rates)
airport_dict = csv_atlas.get_dict()
assert len(airport_dict) is not 0
    
def test_get_airport():      
    assert csv_atlas.get_airport('DUB').get_city() == 'Dublin'
    assert csv_atlas.get_airport('JFK').get_city() == 'New York'
    
# def test_AirportAtlas_list():
#     code_list = csv_atlas.get_code_list()
#     assert code_list[0] == 'HEA'
    
def test_distance():
    airport1 = csv_atlas.get_airport('DUB')
    airport2 = csv_atlas.get_airport('JFK')
    distance = csv_atlas.distance_between_airports(airport1, airport2)
    
    assert int(round(distance, 0)) == 5103
    
def test_rate():
    assert csv_atlas.airport_euro_rate('DUB') == 1

def test_cost():
    assert csv_atlas.cost_between_airports(5103, 1.4) == 7144.2


