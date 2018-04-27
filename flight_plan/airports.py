import os
import csv
from math import pi, sin, cos, acos

class Airport:
    """
    Class for storing and accessing information about an airport
    """
    def __init__(self, name, country, lat, long):
        self._name = name
        self._country = country
        self._latitude = lat
        self._longitude = long
        
    def get_name(self):
        return self._name
    
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
    def __init__(self, ):
        self._euro_rate_dict = {}
    
    def load_data(self, csv_filename):
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
    Stores airport data from CSV file and allows various calculations to be performed on this data
    """   
    def __init__(self, ):
        self._airports_dict = {}
        
    
    def load_data(self, csv_filename):
        """Create dictionary of Airport objects from airports data in CSV file"""
        with open(os.path.join('input', csv_filename), 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for line in reader:
                self._airports_dict[line[4]] = Airport(line[2], line[3], line[6], line[7])
                
                
    def great_circle_distance(self, latitude1, longitude1, latitude2, longitude2):
        """
        Calculates the distance between two sets of geographical coordinates.
        Returns the distance as a float.
        """
        
        R_EARTH = 6371 # radius of earth in km
        theta1 = longitude1 * (2 * pi) / 360
        theta2 = longitude2 * (2 * pi) /360
        phi1 = (90 - latitude1) * (2 * pi) / 360
        phi2 = (90 - latitude2) * (2 * pi) / 360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * R_EARTH
        
        return distance
    
    
    def distance_between_airports(self, airport1, airport2):
        """
        Calculates the distance between two airports.
        Returns the distance as a float.
        """
        distance = self.great_circle_distance(airport1[2], airport1[3], airport2[2], airport2[3])
        return distance
    
    
    def cost_between_airports(self, airport1, airport2):
        """
        Calculates the distance between two airports.
        Returns the distance as a float.
        """
        distance = self.distance_between_airports(airport1, airport2)
        exch_rate = airport1.local_euro_exch_rate(airport1)
        fuel_cost = distance * exch_rate
        return fuel_cost


def main() :
    pass

if __name__ == "main":
    main ()


