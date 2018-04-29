#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for aircrafts module."""

import pytest
import sys
sys.path.append('.')

from flight_plan.aircraft import Aircraft, AircraftDictionary  

# -- Aircraft -- 
def test_Aiport():
    # Create aircraft instance
    params = ('A319', 'jet', 'metric', 'Airbus', 3750)
    aircraft = Aircraft(*params)
    
    # Check methods return correct value
    assert aircraft.get_code() == params[0]
    assert aircraft.get_type() == params[1]
    assert aircraft.get_units() == params[2]
    assert aircraft.get_manufacturer() == params[3]
    assert aircraft.get_range() == params[4]
    
# -- AircraftDictionary --
def test_construct_default_AircraftDictionary():
    aircraft_dict = AircraftDictionary()
    assert aircraft_dict.get_dict() == {}

# Create aircraft dictionary from CSV for use in tests below, and check dict is not empty
csv_aircraft_dict = AircraftDictionary(csv_filename='aircraft.csv')
aircraft_dict = csv_aircraft_dict.get_dict()
assert len(aircraft_dict) is not 0
    
def test_AircraftDictionary_range():
    # metric and first entry so checks field names being skipped correctly  
    assert csv_aircraft_dict.get_aircraft('A319').get_range() == 3750
    # imperial so check metric conversion working
    assert csv_aircraft_dict.get_aircraft('747').get_range() == 18149

