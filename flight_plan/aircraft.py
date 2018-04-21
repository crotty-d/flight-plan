from math import pi , sin , cos , acos

a i r p o r t s=f” JFK ” : ( ” John F Kennedy I n t l ” , ” United S t a te s ” ,40.639751 , −73.778925) ,
”AAL” : ( ” Aalborg ” , ”Denmark” ,57.092789 ,9.849164) ,
”CDG” : ( ” Charles De Gaulle ” , ” France ” ,49.012779 ,2.55) ,
”SYD” : ( ” Sydney I n t l ” , ” A u s t r a l i a ” , −33.946111 ,151.177222) ,
”LHR” : ( ” Heathrow ” , ” United Kingdom” ,51.4775 , −0.461389) ,
”DUB” : ( ” Dublin ” , ” Ireland ” ,53.421333 , −6.270075) ,
”ARN” : ( ” Arlanda ” , ”Sweden” ,59.651944 ,17.918611) ,
” SIN ” : ( ” Changi I n t l ” , ” Singapore ” ,1.350189 ,103.994433) ,
”AMS” : ( ” Schiphol ” , ” Netherlands ” ,52.308613 ,4.763889) ,
”SFO” : ( ” San Francisco I n t l ” , ” United S t a te s ” ,37.618972 , −122.374889)g

def distanceBetweenAirports ( latitude1 , longitude1 , latitude2 , longitude2 ) :
” ” ” C a l c u l a t e s the distance from a second a i r p o r t and returns i t as a f l o a t ” ” ”
# Distance = arccos ( sin phi1 sin phi2 cos ( theta1 − theta2 ) + cos phi1 cos phi2 ) ∗
r a d i u s o f e a r t h
# angles are converted from degrees to radians

r a d i u s e a r t h = 6371 # km
theta1 = longitude1 ∗ (2 ∗ pi ) / 360
theta2 = longitude2 ∗ (2 ∗ pi ) / 360
phi1 = (90 − l a t i t u d e 1 ) ∗ (2 ∗ pi ) / 360
phi2 = (90 − l a t i t u d e 2 ) ∗ (2 ∗ pi ) / 360
distance = acos ( sin ( phi1 ) ∗ sin ( phi2 ) ∗ cos ( theta1 − theta2 ) + cos ( phi1 ) ∗ cos ( phi2 ) ) ∗
r a d i u s e a r t h
return distance

def main () :
a i r p o r t 1=a i r p o r t s . get ( ’DUB ’ )
a i r p o r t 2 = a i r p o r t s . get ( ’SYD ’ )
l a t 1=a i r p o r t 1 [2]
long1 = a i r p o r t 1 [3]
l a t 2 = a i r p o r t 2 [2]
long2 = a i r p o r t 2 [3]
p r i n t ( distanceBetweenAirports ( lat1 , long1 , lat2 , long2 ) )

i f name == ” main ” :
main ()
