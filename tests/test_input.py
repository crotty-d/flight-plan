#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for file input."""

import pytest, sys, os
sys.path.append('.')

repo_dir = os.path.dirname(os.path.dirname(__file__))
csv_dir = os.path.join(repo_dir, 'flight_plan', 'input')

def test_input_data_exsists(): 
    actual_files = os.listdir(csv_dir)
    required_files = ['airport.csv', 'aircraft.csv', 'countrycurrency.csv', 'currencyrates.csv']
    for file in required_files:
        assert file in actual_files        
        
def test_itinerary_input_file_exsists(): 
    actual_files = os.listdir(csv_dir)
    required_file = 'input.csv'
    assert required_file in actual_files