#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for airports module."""

import sys
sys.path.append('.')

from flight_plan.airports import Airport, EuroExchangeRates, AirportAtlas


def test_Aiport():
    # Create airport instance
    params = ('DUB', 'Dublin', 'Ireland', 51.841269, -8.491111)
    airport = Airport(*params)
    
    # Check methods return correct value    
    assert airport.get_code() == params[0]
    assert airport.get_name() == params[1]
    assert airport.get_country() == params[2]
    assert airport.get_latitude() == params[3]
    assert airport.get_longitude() == params[4]
    

