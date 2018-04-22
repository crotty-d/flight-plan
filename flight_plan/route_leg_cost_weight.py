from math import pi, sin, cos, acos
import 

def cost_between_airports(airport1, airport2):
    """
    Calculates the costs between two airports.
    Returns the cost as a float
    """         

    distance = route_leg_distances.getDistance(airport1, airport2)
    
    cost = distance
    
    return cost

def main() :
    airport1 = airports.get('DUB')
    airport2 = airports.get('SYD')
    
    print(cost_between_airports(airport1, airport2))

if __name__ == "main":
    main ()