import os
import csv


class CountryCurrencyCodes:
    """
    Class for storing and accessing the currency codes of all countries.
    
    Can take country and currency code from CSV file.
    """
    
    # Dictionary to store country and currency code
    _code_dict = {}
    
    def __init__(self, currency_code_dict={}, csv_filename:str=None):
        """
        Create CountryCurrencyCodes object.
        
        Default is empty dictionary.
        Set csv_filename parameter to construct dictionary from the CSV
        """
        try:
            if csv_filename is not None: #TODO: handle missing
                with open(os.path.join('/home/d/Git/flight_plan/flight_plan/input', csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
                    reader = csv.reader(f)
                    next(reader) # skip field names (first row)
                    for line in reader:
                        self._code_dict[line[0]] = line[14]
            else:           
                self._code_dict = currency_code_dict
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
    
    def __init__(self, euro_rate_dict={}, csv_filename:str=None):
        """
        Create EuroRates object.
        
        Default is empty dictionary.
        Set csv_filename parameter to construct dictionary from the CSV
        """
        try:
            if csv_filename is not None: #TODO: handle missing
                with open(os.path.join('/home/d/Git/flight_plan/flight_plan/input', csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
                    reader = csv.reader(f)
                    for line in reader:
                        self._rate_dict[line[1]] = float(line[2])
            else:           
                self._rate_dict = euro_rate_dict
        except IOError as e:
            print(e)
            
    def get_dict(self):
        return self._rate_dict
        
    def get_rate(self, currency_code:str):
        return self._rate_dict[currency_code]
    