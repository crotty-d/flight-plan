# airports = {" JFK " : ( " John F Kennedy I n t l " , " United S t a te s " ,40.639751 , −73.778925) ,
# "AAL" : ( " Aalborg " , "Denmark" ,57.092789 ,9.849164) ,
# "CDG" : ( " Charles De Gaulle " , " France " ,49.012779 ,2.55) ,
# "SYD" : ( " Sydney I n t l " , " A u s t r a l i a " , −33.946111 ,151.177222) ,
# "LHR" : ( " Heathrow " , " United Kingdom" ,51.4775 , −0.461389) ,
# "DUB" : ( " Dublin " , " Ireland " ,53.421333 , −6.270075) ,
# "ARN" : ( " Arlanda " , "Sweden" ,59.651944 ,17.918611) ,
# " SIN " : ( " Changi I n t l " , " Singapore " ,1.350189 ,103.994433) ,
# "AMS" : ( " Schiphol " , " Netherlands " ,52.308613 ,4.763889) ,
# "SFO" : ( " San Francisco I n t l " , " United S t a te s " ,37.618972 , −122.374889)}

from math import pi, sin, cos, acos
   

def great_circle_distance(latitude1, longitude1, latitude2, longitude2):
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


def distance_between_airports(airport1, airport2):
    pass


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


