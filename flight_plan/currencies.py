# -*- coding: utf-8 -*-

import os
import csv


class CountryCurrencyCodes:
    """
    Class for storing and accessing the currency codes of all countries.
    
    Can take country and currency code from CSV file.
    """
    
    # Dictionary to store country and currency code
    _code_dict = {}
    # Default directories for input data
    _default_dir = os.path.dirname(__file__)
    _default_input_dir = os.path.join(_default_dir, 'input')
    
    def __init__(self, currency_code_dict={}, csv_filename:str=None, input_dir=_default_input_dir):
        """
        Create CountryCurrencyCodes object.
        
        Default is empty dictionary.
        Set csv_filename parameter to construct dictionary from the CSV
        """
        if csv_filename is not None:
            self.load_data(csv_filename, input_dir)
        else:           
            self._code_dict = currency_code_dict
            
            
    def load_data(self, csv_filename, input_dir):
        try:
            with open(os.path.join(input_dir, csv_filename), 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                next(reader) # skip field names (first row)
                for line in reader:
                    self._code_dict[line[0]] = line[14]
        except IOError as e:
            print(e)
                      
        
    def get_dict(self):
        return self._code_dict
    
    
    def get_code(self, country:str):
        return self._code_dict[country]
    

class EuroRates:
    """
    Class for storing and accessing the euro exchange rates for all currencies (from euro to currency).
    
    Can take country and currency code from CSV file.
    Currencies represented by their 3-character alphabetic code.
    """
    
    # Dictionary to store euro exchange rate
    _rate_dict = {}
    # Default directories for input data
    _default_dir = os.path.dirname(__file__)
    _default_input_dir = os.path.join(_default_dir, 'input')
    
    
    def __init__(self, euro_rate_dict={}, csv_filename:str=None, input_dir=_default_input_dir):
        """
        Create EuroRates object.
        
        Default is empty dictionary.
        Set csv_filename parameter to construct dictionary from the CSV
        """
        
        if csv_filename is not None: #TODO: handle missing
            self.load_data(csv_filename, input_dir)
        else:           
            self._rate_dict = euro_rate_dict
            
            
    def load_data(self, csv_filename, input_dir):
        try:
            with open(os.path.join(input_dir, csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
                reader = csv.reader(f)
                for line in reader:
                    self._rate_dict[line[1]] = float(line[2])
        except IOError as e:
            print(e)    
            
    def get_dict(self):
        return self._rate_dict
    
        
    def get_rate(self, currency_code:str):
        return self._rate_dict[currency_code]
    