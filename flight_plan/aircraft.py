class Aircraft:
    """
    Aircraft class: An Airplane has to be fueled before it can takeoff
    """
    
    __MINFUEL = 100 # minimum amount of fuel for take off no matter what aircraft

    def init(self, flightNumber=""):
        self.flightNumber = flightNumber # you must have a flight number assigned to fly
        self.fuel = 0    # private attribute containing current fuel in aircraft
        self.fuelCheck = False    # this is a boolean flag for a preflight check .
        self.maxFuel = self.MINFUEL

    def fuelCheck(self):
        if self.fuel < self.MINFUEL:
            print("[", self.flightNumber,"] Fuel  Check  Failed: Current  fuel  below  safe  limit: ", self.fuel, /
            "less than", self.MINFUEL)
            self.fuelCheck = False
        else:
            print("[", self.flightNumber,"] Fuel check complete. Current  fuel  level: ",  self.fuel)
            self.fuelCheck = True
            
        return self.fuelCheck

    def takeOff(self):
        if self.fuelCheck() == True:
            print("[", self.flightNumber, "] Cleared for takeoff!")
        else:
            print("[", self.flightNumber, "] Take off Failed: complete pre-flight fuel check and refuel first")
            print(self.fuelCheck())
    
    def printFuelLevel(self):
        print("Current  fuel: ",  self.fuel)

    def addFuel(self, volume):
        
        unusedFuel = 0

        if volume < 0:
            print("No syphoning fuel!")
        elif self.fuel + volume <= self.maxFuel:
            self.fuel  =  self.fuel + volume
        elif self.fuel + volume > self.maxFuel:
            self.fuel = self.maxFuel
        
        unusedFuel = volume - self.fuel            
        return unusedFuel

class Airplane(Aircraft):
    """
    An Airplane is a type of aircraft (it has two wings and can fly)
    """

    def init(self, flightnumber=""):
        Aircraft.init(self, flightnumber)
        self.maxFuel = 5000
        # print(self.maxFuel)

class Helicopter(Aircraft):
    """
    A Helicopter is a type of aircraft(it has a rotor and a smaller fuel capacity than an airplane)
    """
    def init(self, flightnumber=""):
        Aircraft.init(self, flightnumber)
        self.maxFuel = 1000
        print(self.maxFuel)