import os
import csv
import collections
import itertools

from flight_plan.airports import Airport, AirportAtlas
from flight_plan.currencies import CountryCurrencyCodes, EuroRates

  
class RouteCostGraph:
    """ 
    Undirected graph of airports for calculating different itinerary costs.
    
    Weighted by fuel cost (inter-airport distance * Euro conversion rate).
    """

    def __init__(self, airport_atlas): #TODO: take in dict or list
        self.vertices = set()

        # Default value for all vertices set as empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}
        
        #TODO: Loops to generate graph from AirportAtlas using add edge and vertex methods
        pass
 
    def add_vertex(self, airport):
        self.vertices.add(airport)
        
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


class Itinerary:
    """...""" #FIXME
    
    __airport_list = []

    def __init__(self, airport_list=[], csv_filename=None):
        """
        Create Itinerary object.
        
        Default is empty list.
        Dictionary values must be Airport objects.
        Set csv_filename parameter to construct dictionary from the csv
        """
        
        if csv_filename is not None:
            with open(os.path.join('/home/d/Git/flight_plan/flight_plan/input', csv_filename), 'rt', encoding='utf8') as f: #FIXME: relative path
                reader = csv.reader(f)
                row_idx = 0
                for line in reader:
                    self._airport_list[row_idx] = [field for field in line]
                    row_idx += 1
        else:
            self._airport_list = airport_list
        
    def all_permutations(self): # TODO: limit to perms starting and ending on home
        
        permutations = itertools.permutations(self.airport_list[1:-1])
        
        return list(permutations)
        
    def cheapest_routes(self, route_cost_graph): # TODO: cost graph as param of init?
        # TODO: add code to calculate cheapest route via route_cost_graph
        routes = [] #FIXME: placeholder
        costs = [] #FIXME: placeholder
        
        return {'cheapest routes': cheapest_routes, 'costs': costs}
    
    # TODO: shortest route method?
    
    
    

    