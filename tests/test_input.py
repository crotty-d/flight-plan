#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for file input."""

import pytest, sys, os
sys.path.append('.')


def test_input_data_exsists(): 
    actual_files = os.listdir('/home/d/Git/flight_plan/flight_plan/input') # FIXME: make path relative
    required_files = ['airport.csv', 'countrycurrency.csv', 'currencyrates.csv']
    for file in required_files:
        assert file in actual_files        
        
def test_itinerary_input_file_exsists(): 
    actual_files = os.listdir('/home/d/Git/flight_plan/flight_plan/input') # FIXME: make path relative
    required_file = 'input.csv'
    assert required_file in actual_files