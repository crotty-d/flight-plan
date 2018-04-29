import os
import csv
import collections
import itertools

from flight_plan.airports import Airport, AirportAtlas
from flight_plan.currencies import CountryCurrencyCodes, EuroRates

  
class RouteCostGraph: #TODO: Distance graph with g.cirrcle and distance methods. RCG inherits from this adding cost method and modifying weights
    """ 
    Undirected graph of airports for calculating different itinerary costs.
    
    Weighted by fuel cost (inter-airport distance * Euro conversion rate).
    """

    def __init__(self, airport_atlas): #TODO: take in dict or list?
        self.vertices = set()

        # Default value for all vertices set as empty list
        self.edges = collections.defaultdict(list) #TODO: Private edges and vertices? getters only?
        self.weights = {}
        
        #TODO: Loops to generate graph from AirportAtlas using add edge and vertex methods
        pass
 
    def add_vertex(self, airport):
        self.vertices.add(airport.get_code())
        
    def cost_between_airports(self, airport1, airport2):
        """
        Return the (fuel) cost between two airports as a float.
        """
        distance = AirportAtlas.distance_between_airports(airport1, airport2)
        origin_country = airport1.get_country()
        origin_currency_code = CountryCurrencyCodes.get_code(origin_country)
        origin_exch_rate = EuroRates.get_rate(origin_currency_code)
        fuel_cost = distance * origin_exch_rate
        return fuel_cost
 
    def add_edge(self, from_vertex, to_vertex): # TODO: from/to_airport not vertex?
        if from_vertex != to_vertex: # no self edges
            self.edges[to_vertex].append(from_vertex)
            self.weights[(from_vertex, to_vertex)] = self.cost_between_airports(from_vertex, to_vertex)
            self.weights[(to_vertex, from_vertex)] = self.cost_between_airports(to_vertex, from_vertex)
 
    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


class Itineraries:
    """...""" #FIXME
    
    _itinerary_list = []

    def __init__(self, itinerary_list=[], csv_filepath=None):
        """
        Create Itineraries object.
        
        Default is empty list.
        Dictionary values must be Airport objects.
        Set csv_filename parameter to construct dictionary from the csv
        """
        
        if csv_filepath is not None:
            with open(csv_filepath) as f: #FIXME: relative path
                reader = csv.reader(f)
                row_idx = 0
                for line in reader:
                    self._itinerary_list[row_idx] = [field for field in line]
                    row_idx += 1
        else:
            self._itinerary_list = itinerary_list
        
    def get_itinerary_list(self):
        return self._itinerary_list
    
    def route_permutations(self): # TODO: limit to perms starting and ending on home
        origin = self._itinerary_list[0]
        route_permutations = []
        
        for itinerary in self._itinerary_list:
            # Get list of all permutations of intermediary airpoirts
            permutations = itertools.permutations(self._itinerary_list[1:-2])
            # Book-end list with origin airport to complete routes
            for p in permutations:
                p.insert(0, origin)
                p.append(origin)
            
            route_permutations.append(permutations)     
        
        return route_permutations
        
    def cheapest_route(self, route_permutations, aircraft, cost_graph): # TODO: check aircraft range against distance graph
        # TODO: add code to calculate cheapest route via cost (and distance) graphs
        route = [] #FIXME: placeholder
        cost = 0 #FIXME: placeholder
        
        return route.append(cost)
    
    # TODO: shortest route method?
    
    
    

    