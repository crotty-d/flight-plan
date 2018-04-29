#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for airports module."""

import pytest
import sys
sys.path.append('.')

from flight_plan.airports import Airport, AirportAtlas  

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
def test_construct_default_AirportAtlas():
    atlas = AirportAtlas()
    assert atlas.get_dict() == {}

# Create airport atlas from CSV for use in tests below, and check dict is not empty
csv_atlas = AirportAtlas(csv_filename='airport.csv')
airport_dict = csv_atlas.get_dict()
assert len(airport_dict) is not 0
    
def test_AirportAtlas_dict():      
    assert csv_atlas.get_airport('DUB').get_city() == 'Dublin'
    assert csv_atlas.get_airport('JFK').get_city() == 'New York'
    
def test_distance():
    airport1 = csv_atlas.get_airport('DUB')
    airport2 = csv_atlas.get_airport('JFK')
    distance = csv_atlas.distance_between_airports(airport1, airport2)
    
    assert int(round(distance, 0)) == 5103


