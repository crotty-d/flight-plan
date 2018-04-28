import os
import csv
from math import pi, sin, cos, acos

class Airport:
    """
    Class for storing and accessing information about an airport
    """
    def __init__(self, code: str, city: str, country: str, lat: float, long: float):
        self._code = code
        self._city = city
        self._country = country
        self._latitude = lat
        self._longitude = long
        
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
    

class EuroExchangeRates: #FIXME: Complete class
    """
    Stores country euro exchange rate data from CSV file
    """   
    def __init__(self):
        self._euro_rate_dict = {}
    
    def load_data(self, csv_filename: str):
        """...."""
        with open(os.path.join('input', csv_filename), 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for line in reader:
                self._euro_rate_dict[line[4]] = Airport(line[2], line[3], line[6], line[7])
                
    def local_euro_exch_rate(self, country):
        # TODO: get country for each airport and then
        exch_rate = 1 # FIXME: placeholder
        return exch_rate
    
   
class AirportAtlas:
    """
    Stores airport data in a dictionary of airport objects.
    
    Provides methods to perform various calculations on this data,
    and a method ro load in airport data from a CSV file.
    """   
        
    def __init__(self, dict_of_Airports={}):
        """
        Create instance of AirportAtlas comprising dictionary of Airport instances.
        
        Default is empty dictionary.
        Dictionary values must be instances of the Airport object.
        """
                   
        self._airports_dict = dict_of_Airports
    
    def load_csv(self, csv_filename: str):
        """Create dictionary of Airport instances from airports data in CSV file"""
        with open(os.path.join('/home/d/Git/flight_plan/flight_plan/input', csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
            reader = csv.reader(f)
            for line in reader:
                self._airports_dict[line[4]] = Airport(line[4], line[2], line[3], float(line[6]), float(line[7]))                
                
    def getDict(self):
        """Return dictionary of Airport instances for all airports in atlas"""
        return self._airports_dict
    
    def get_airport(self, airport_code):
        """Return Airport instance specified in airport code parameter"""
        return self._airports_dict[airport_code]
    
    def great_circle_distance(self, latitude1, longitude1, latitude2, longitude2):
        """
        Return the distance between two sets of geographical coordinates as a float.
        
        All parameters are floats.
        """        
        R_EARTH = 6371 # radius of earth in km
        print(longitude1)
        theta1 = longitude1 * (2 * pi) / 360
        theta2 = longitude2 * (2 * pi) / 360
        phi1 = (90 - latitude1) * (2 * pi) / 360
        phi2 = (90 - latitude2) * (2 * pi) / 360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * R_EARTH
        
        return distance    
    
    def distance_between_airports(self, airport1, airport2):
        """
        Return the distance between two airports as a float.
        """
        distance = self.great_circle_distance(airport1.get_latitude(), airport1.get_longitude(), airport2.get_latitude(), airport2.get_longitude())
        return distance    
    
    def cost_between_airports(self, airport1, airport2):
        """
        Return the (fuel) cost between two airports as a float.
        """
        distance = self.distance_between_airports(airport1, airport2)
        exch_rate = airport1.local_euro_exch_rate(airport1)
        fuel_cost = distance * exch_rate
        return fuel_cost

def main() :
    a = AirportAtlas()
    print(a.getDict())

if __name__ == "main":
    main ()


