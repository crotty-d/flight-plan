#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Currencys module."""

import pytest
import sys
sys.path.append('.')

from flight_plan.currencies import Currency, CurrenciesInfo

# -- Currency -- 
def test_Currency(): #FIXME complete (copypasted from test_airports
    # Create Currency instance
    params = ('GBP', '', 'Ireland', 51.841269, -8.491111)
    Currency = Currency(*params)
    
    # Check methods return correct value
    assert Currency.get_code() == params[0]
    assert Currency.get_city() == params[1]
    assert Currency.get_country() == params[2]
    assert Currency.get_latitude() == params[3]
    assert Currency.get_longitude() == params[4]
    
# -- CurrenciesInfo --
def test_default_CurrenciesInfo_construct():
    default_atlas = CurrenciesInfo()
    assert default_atlas.getDict() == {}, 'Returned: {}'.format(default_atlas.getDict)

def test_CurrenciesInfo_construct_from_csv():   
    csv_atlas = CurrenciesInfo(csv_filename='Currency.csv')
    Currency_dict = csv_atlas.getDict()
    assert Currency_dict is not {}
    
    return csv_atlas

# Create Currency atlas from CSV for use in tests below
csv_atlas = test_CurrenciesInfo_construct_from_csv()
    
def test_CurrenciesInfo_dict():
    Currencys_dict = csv_atlas.getDict()
    Currency_code1 = 'DUB'
    Currency_code2 = 'JFK'      
    assert Currencys_dict[Currency_code1].get_city() == 'Dublin'
    assert Currencys_dict[Currency_code2].get_city() == 'New York'

    
def test_distance():
    Currency1 = csv_atlas.get_Currency('DUB')
    Currency2 = csv_atlas.get_Currency('JFK')
    distance = csv_atlas.distance_between_Currencys(Currency1, Currency2)
    
    assert int(round(distance, 0)) == 5103

