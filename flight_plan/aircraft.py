class Aircraft:
    """
    Aircraft class: An Airplane has to be _fueled before it can takeoff
    """
    
    __MIN_fuel = 100 # minimum amount of _fuel for take off no matter what aircraft

    def init(self, flightNumber=""):
        self.flightNumber = flightNumber # you must have a flight number assigned to fly
        self._fuel = 0    # private attribute containing current _fuel in aircraft
        self._fuelCheck = False    # this is a boolean flag for a preflight check .
        self.max_fuel = self.MIN_fuel

    def _fuelCheck(self):
        if self._fuel < self.MIN_fuel:
            print("[", self.flightNumber,"] Fuel below safe limit: ", self._fuel, \
            "less than", self.MIN_fuel)
            self._fuelCheck = False
        else:
            print("[", self.flightNumber,"] Fuel check complete. Current fuel: ", self._fuel)
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
        # print(self.max_fuel)

class Helicopter(Aircraft):
    """
    A Helicopter is a type of aircraft(it has a rotor and a smaller fuel capacity than an airplane)
    """
    def init(self, flightnumber=""):
        Aircraft.init(self, flightnumber)
        self.max_fuel = 1000
        print(self.max_fuel)