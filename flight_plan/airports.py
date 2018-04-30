# -*- coding: utf-8 -*-

import os
import csv
from math import pi, sin, cos, acos

class Airport:
    """
    Class for storing and accessing information about an airport.
    
    Latitude and longitude parameters can be a float, int or string representation of a number;
    will be converted to float.
    """
    def __init__(self, code:str, city:str, country:str, lat:float, long:float):
        self._code = code
        self._city = city
        self._country = country
        self._latitude = float(lat)
        self._longitude = float(long)
        
    def get_code(self):
        return self._code
    
    def get_city(self):
        return self._city
        
    def get_country(self):
        return self._country
    
    def get_latitude(self):
        return self._latitude
    
    def get_longitude(self):
        return self._longitude  
 
   
class AirportAtlas:
    """
    Stores airport data from CSV file in a dictionary of airport objects.
    
    Also provides methods to perform various calculations on this data.
    """
    
    # Dictionary to store Airport objects
    _airports_dict = {}
    # Default directories for input data
    _default_dir = os.path.dirname(__file__)
    _default_input_dir = os.path.join(_default_dir, 'input')
        
    def __init__(self, csv_filename:str, country_curr_codes, euro_rates, input_dir=_default_input_dir):
        """
        Create instance of AirportAtlas comprising dictionary of Airport objects.
        
        Default is empty dictionary.
        Dictionary values must be Airport objects.
        Set csv_filename parameter to construct dictionary from the csv
        """
        self.load_data(csv_filename, input_dir)
        self._country_curr_codes = country_curr_codes
        self._euro_rates = euro_rates
        
            
    def load_data(self, csv_filename:str, input_dir):
        """Load data from CSV file"""
        try:    
            with open(os.path.join(input_dir, csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
                reader = csv.reader(f)
                for line in reader:
                    self._airports_dict[line[4]] = Airport(line[4], line[2], line[3], line[6], line[7])    
        except IOError as e:
            print(e)
            
    
    def get_dict(self):
        """Return dictionary of Airport objects for all airports in atlas"""
        return self._airports_dict
    
    
    def get_code_list(self):
        """Return list of airport codes for all airports in atlas"""
        return self._airport_code_list
    
    
    def get_airport(self, airport_code:str):
        """Return Airport instance specified in airport code parameter"""
        return self._airports_dict[airport_code]
    
    
    def great_circle_distance(self, latitude1, longitude1, latitude2, longitude2):
        """
        Return the distance between two sets of geographical coordinates as a float.
        
        All parameters are floats.
        """        
        R_EARTH = 6371 # radius of earth in km
        theta1 = longitude1 * (2 * pi) / 360
        theta2 = longitude2 * (2 * pi) / 360
        phi1 = (90 - latitude1) * (2 * pi) / 360
        phi2 = (90 - latitude2) * (2 * pi) / 360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * R_EARTH
        return distance  
      
    
    def distance_between_airports(self, airport_code1, airport_code2):
        """
        Return the distance between two airports as a float.
        """
        airport1 = self._airports_dict[airport_code1]
        airport2 = self._airports_dict[airport_code2]
        coordinates = (airport1.get_latitude(), airport1.get_longitude(), airport2.get_latitude(), airport2.get_longitude())
        distance = self.great_circle_distance(*coordinates)
        return distance    
    
    
    def airport_euro_rate(self, airport_code):
        """
        Return the euro exchange rate at the given airport
        """
        airport = self._airports_dict[airport_code]
        country = airport.get_country()
        currency_code = self._country_curr_codes.get_code(country)
        exch_rate = self._euro_rates.get_rate(currency_code)
        return exch_rate
    
    
    def cost_between_airports(self, distance, exch_rate):
        """
        Return the distance between two airports as a float.
        """
        return distance * exch_rate

