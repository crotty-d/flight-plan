import os
import csv
from math import pi, sin, cos, acos

class Aircraft:
    """
    Class for storing and accessing information about an aircraft.
    
    Range parameter can be a float, int or string representation of a number;
    will be converted to int.
    """
    def __init__(self, code:str, aircraft_type:str, units:str, manufacturer:str, aircraft_range:int):
        self._code = code
        self._aircraft_type = aircraft_type
        self._units = units
        self._manufacturer = manufacturer
        # Convert range to km if in imperial units (nautical miles)
        if self._units.lower() == 'imperial':
            self._aircraft_range = int(float(aircraft_range) * 1.852)
        else:
            self._aircraft_range = int(aircraft_range)
        
    def get_code(self):
        return self._code
    
    def get_type(self):
        return self._aircraft_type
        
    def get_units(self):
        return self._units
    
    def get_manufacturer(self):
        return self._manufacturer
    
    def get_range(self):
        return self._aircraft_range 
 
   
class AircraftDictionary:
    """
    Stores aircraft data in a dictionary of aircraft objects.
    
    Also provides methods to perform various calculations on this data.
    """
    
    # Dictionary to store Airport objects
    _aircraft_dict = {}               
        
    def __init__(self, aircraft_dict={}, csv_filename:str=None):
        """
        Create instance of AirportAtlas comprising dictionary of Airport objects.
        
        Default is empty dictionary.
        Dictionary values must be Airport objects.
        Set csv_filename parameter to construct dictionary from the csv
        """
        if csv_filename is not None:
            self.load_data(csv_filename)
        else:           
            self._aircraft_dict = aircraft_dict
            
            
    def load_data(self, csv_filename:str=None):
        """Load data from CSV file"""
        try:    
            with open(os.path.join('/home/d/Git/flight_plan/flight_plan/input', csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
                reader = csv.reader(f)
                next(reader) # skip field names (first row)
                for line in reader:
                    self._aircraft_dict[line[0]] = Aircraft(line[0], line[1], line[2], line[3], line[4])    
        except IOError as e:
            print(e)
            
    
    def get_dict(self):
        """Return dictionary of Airport instances for all aircraft in atlas"""
        return self._aircraft_dict
    
    
    def get_aircraft(self, aircraft_code:str):
        """Return Airport instance specified in aircraft code parameter"""
        return self._aircraft_dict[aircraft_code]
    
    