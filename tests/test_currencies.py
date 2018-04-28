#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for currencies module."""

import pytest
import sys
sys.path.append('.')

from flight_plan.currencies import CountryCurrencyCodes, EuroRates

   
# -- CountryCurrencyCodes --
def test_construct_default_country_currency_codes():
    currency_codes = CountryCurrencyCodes()
    assert currency_codes.get_dict() == {}

def test_construct_country_currency_codes_from_csv():   
    currency_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
    code_dict = currency_codes.get_dict()
    assert currency_codes is not {}
    
    return currency_codes

# Create CountryCurrencyCodes object from CSV for use in tests below
csv_codes = test_construct_country_currency_codes_from_csv()
    
def test_country_currency_get_code():   
    assert csv_codes.get_code('Ireland') == 'EUR'


# -- EuroRates --
def test_construct_default_euro_rates():
    euro_rates = EuroRates()
    assert euro_rates.get_dict() == {}

def test_construct_euro_rates_from_csv():   
    euro_rates = EuroRates(csv_filename='currencyrates.csv')
    rate_dict = euro_rates.get_dict()
    assert rate_dict is not {}
    
    return euro_rates

# Create EuroRates object from CSV for use in tests below
csv_rates = test_construct_euro_rates_from_csv()
    
def test_euro_rates_get_code():   
    assert csv_rates.get_rate('EUR') == 1.0
    assert csv_rates.get_rate('USD') == 0.9488

