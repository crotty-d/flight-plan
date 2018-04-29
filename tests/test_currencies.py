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

# Create CountryCurrencyCodes object from CSV for use in tests below
csv_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
code_dict = csv_codes.get_dict()
assert len(code_dict) is not 0
    
def test_country_currency_get_code():
    # First entry so checks field names being skipped correctly
    assert csv_codes.get_code('Afghanistan') == 'AFN'
    # Check another entry
    assert csv_codes.get_code('Ireland') == 'EUR'


# -- EuroRates --
def test_construct_default_euro_rates():
    euro_rates = EuroRates()
    assert euro_rates.get_dict() == {}

# Create EuroRates object from CSV for use in tests below, and check dict not empty
csv_rates = EuroRates(csv_filename='currencyrates.csv')
rate_dict = csv_rates.get_dict()
assert len(rate_dict) is not 0
    
def test_euro_rates_get_code():   
    assert csv_rates.get_rate('EUR') == 1.0
    assert csv_rates.get_rate('USD') == 0.9488

