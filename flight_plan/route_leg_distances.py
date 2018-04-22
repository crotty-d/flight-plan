from math import pi, sin, cos, acos

def distance_between_goecoords(latitude1, longitude1, latitude2, longitude2):
    """
    Calculates the distance between two sets of geographical coordinates.
    Returns the distance as a float
    """
    
    # Distance = arccos(sinphi1 sinphi2 cos(theta1 - theta2) + cosphi1 cosphi2) * radiusofearth
    # anglesareconvertedfromdegreestoradians
    
    R_EARTH = 6371 # km
    theta1 = longitude1 * (2 * pi)/360
    theta2 = longitude2 * (2 * pi)/360
    phi1 = (90 - latitude1) * (2 * pi)/360
    phi2 = (90 - latitude2) * (2 * pi)/360
    distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * R_EARTH
    
    return distance

def main() :
    airport1 = airports.get('DUB')
    airport2 = airports.get('SYD')
    lat1 = airport1[2]
    long1 = airport1[3]
    lat2 = airport2[2]
    long2 = airport2[3]
    print(distance_between_goecoords(lat1, long1, lat2, long2))

if __name__ == "main":
    main ()