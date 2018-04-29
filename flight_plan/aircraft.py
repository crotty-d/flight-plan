import csv
from math import pi, sin, cos, acos

class Airport:
    """
    Class for storing and accessing information about an aircraft.
    
    Range parameter can be a float, int or string representation of a number;
    will be converted to int.
    """
    def __init__(self, code: str, city: str, country: str, lat: float, long: float):
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
    Stores airport data in a dictionary of airport objects.
    
    Also provides methods to perform various calculations on this data.
    """
    
    # Dictionary to store Airport objects
    _airports_dict = {}               
        
    def __init__(self, dict_of_Airports={}, csv_filename:str=None):
        """
        Create instance of AirportAtlas comprising dictionary of Airport objects.
        
        Default is empty dictionary.
        Dictionary values must be Airport objects.
        Set csv_filename parameter to construct dictionary from the csv
        """
        if csv_filename is not None:
            self.load_data(csv_filename)
        else:           
            self._airports_dict = dict_of_Airports
            
            
    def load_data(self, csv_filename:str=None):
        """Load data from CSV file"""
        try:    
            with open(os.path.join('/home/d/Git/flight_plan/flight_plan/input', csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
                reader = csv.reader(f)
                for line in reader:
                    self._airports_dict[line[4]] = Airport(line[4], line[2], line[3], line[6], line[7])    
        except IOError as e:
            print(e)
            
    
    def get_dict(self):
        """Return dictionary of Airport instances for all airports in atlas"""
        return self._airports_dict
    
    
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
      
    
    def distance_between_airports(self, airport1, airport2):
        """
        Return the distance between two airports as a float.
        """
        coordinates = (airport1.get_latitude(), airport1.get_longitude(), airport2.get_latitude(), airport2.get_longitude())
        distance = self.great_circle_distance(*coordinates)
        return distance    
    


.flightNumber,"] Fuel check complete. Current fuel: ", self._fuel)
            self._fuelCheck = True
            
        return self._fuelCheck

    def takeOff(self):
        if self._fuelCheck() == True:
            print("[", self.flightNumber, "] Cleared for takeoff!")
        else:
            print("[", self.flightNumber, "] Take off Failed: complete pre-flight _fuel check and refuel first")
            print(self._fuelCheck())
            
    
    def print_fuelLevel(self):
        print("Current fuel: ",  self._fuel)
        

    def add_fuel(self, volume):
        
        unused_fuel = 0

        if volume < 0:
            print("Error: Fuel cannot be < 0")
        elif self._fuel + volume <= self.max_fuel:
            self._fuel = self._fuel + volume
        elif self._fuel + volume > self.max_fuel:
            self._fuel = self.max_fuel
        
        unused_fuel = volume - self._fuel            
        return unused_fuel
    

class Airplane(Aircraft):
    """
    An Airplane is a type of aircraft (it has two wings and can fly)
    """

    def init(self, flightnumber=""):
        Aircraft.init(self, flightnumber)
        self.max_fuel = 5000
        

class Helicopter(Aircraft):
    """
    A Helicopter is a type of aircraft(it has a rotor and a smaller fuel capacity than an airplane)
    """
    def init(self, flightnumber=""):
        Aircraft.init(self, flightnumber)
        self.max_fuel = 1000
        print(self.max_fuel)