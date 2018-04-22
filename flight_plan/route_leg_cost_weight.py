import route_leg_distances
import airports

def cost_between_airports(airport1, airport2):
    """
    Calculates the costs between two airports.
    Returns the cost as a float
    """         

    distance = route_leg_distances.getDistance(airport1, airport2)
    
    cost = distance * this.get_cost_weight(airport1, airport2)
    
    return cost

def main() :
    airport1 = airports.get('DUB')
    airport2 = airports.get('SYD')
    
    print(cost_between_airports(airport1, airport2))

if __name__ == "main":
    main ()