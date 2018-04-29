import os
import csv
import collections
import itertools

from flight_plan.airports import Airport, AirportAtlas
from flight_plan.currencies import CountryCurrencyCodes, EuroRates
from flight_plan.aircraft import AircraftDictionary

  
class RouteCostGraph: #TODO: RouteGraph as includes distance
    """ 
    Mixed multigraph of airports for calculating different itinerary costs.
    
    Three edges connect each node (airport code): one undirected edge weighted by great-circle distance,
    and two oppositely directed edges weighted by fuel cost (inter-airport distance * Euro conversion rate).
    """

    def __init__(self): #TODO: take in dict or list?
        self.nodes = [] # list used over set as faster to iterate through when creating edges from nodes

        # Each edge initialised as empty list
        self._triple_edges = collections.defaultdict(list) #TODO: Private edges and nodes? getters only?
        # Weights initialised as as empty dictionaries
        self._distances = {}
        self._costs = {}
        
 
    def add_node(self, airport):
        self._nodes.add(airport.get_code())
        
    def airport_euro_rate(self, airport):
        """
        Return the (fuel) cost between two airports as a float.
        """
        country = airport.get_country()
        currency_code = CountryCurrencyCodes.get_code(country)
        exch_rate = EuroRates.get_rate(currency_code)
        return exch_rate
 
 
    def add_edge(self, from_node, to_node): # TODO: from/to_airport not node?
        
        if from_node != to_node: # no self edges
            self._triple_edges[to_node].append(from_node)
            # Distance weight
            distance = AirportAtlas.distance_between_airports(from_node, to_node)
            self._distances[(from_node, to_node)] = self._distances[(to_node, from_node)] = distance
            # Cost weights
            self._costs[(from_node, to_node)] = self.airport_euro_rate(from_node) * distance
            self._costs[(to_node, from_node)] = self.airport_euro_rate(from_node) * distance
    
            
    def bulid_from_atlas(self, airport_atlas):
        """Add nodes and edges based on entire contents of AirportAtlas object"""
        # List of airport codes 
        code_list = airport_atlas.get_list()
        # Add nodes
        for airport_code in code_list:
            self.add_node(airport_code)
        # Add edges between all (unordered) pairs of nodes (airport codes)
        all_node_pairs = list(itertools.combinations(code_list, 2))
        for pair in all_node_pairs:
            self.add_edge(*pair)
            
    
    def get_distance(self, airport1, airport2):
        return self._distances[(airport1, airport1)]
    
    def get_cost(self, airport1, airport2):
        return self._costs[(airport1, airport1)]
 
    def __str__(self):
        string = "Vertices: " + str(self._nodes) + "\n"
        string += "Edges: " + str(self._edges) + "\n"
        string += "Weights: " + str(self._weights)
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
        """
        Get all route permutations for each item in itinerary list
        
        Returns list of permutation lists
        """
        route_permutations = []
        
        for itinerary in self._itinerary_list:
            origin = self.itinerary[0]
            aircraft_code = self.itinerary[-1]
            # Get list of all permutations (tuples) of intermediary airports
            permutations = list(itertools.permutations(itinerary[1:-2]))
            # Book-end list with origin airport to complete routes
            for p in permutations:
                p.insert(0, origin)
                p.append(origin)
                p.append(aircraft_code)
            
            route_permutations.append(permutations)     
        
        return route_permutations
        
    def best_routes(self, route_permutations, route_graph, aircraft_dict): # TODO: check aircraft range against distance graph
        """
        For each itinerary, get cheapest viable route based on the possible permutations.
        
        Returns list of best routes, one for each itinerary.
        """        
        # Go through list of permutations of for each itinerary to find best route
        best_routes = []
        for itinerary in route_permutations: # TODO: Maybe Numpy or Pandas here?
            # Aircraft range (limits possible routes)
            aircraft_code = self.itinerary[-1]
            aircraft_range = aircraft_dict.get_aircraft(aircraft_code).get_range()
            # Initialise variables; min value as high as possible
            infinity = float('+inf')
            min_route_cost = infinity
            # Get cheapest route in itinerary
            for route in itinerary:
                cost_route = 0
                route_not_viable = False
                # Add up cost of route legs
                for i in range(len(route)-2): # exclude final destination and aircraft code
                    distance_leg = route_graph.get_cost(route[i], route[i+1])
                    if distance_leg > aircraft_range:
                        route_not_viable = True
                        break
                    else:
                        cost_route += route_graph.get_cost(route[i], route[i+1])
                if route_not_viable == False and cost_route < min_route_cost:
                    best_route = route
                    min_cost = cost_route
                    cost_route = 0 # reset cost counter
            # If viable route found, ...
            if min_route_cost != infinity:
                # ...assign as best route for that itinerary...
                best_routes.append(best_route)
                # ...and add cost to end of route
                best_route.append(min_cost)
            else:
                # ...use input itinerary and...
                best_routes.append(best_route)
                # ...add 'No viable route' to end
                best_route.append('No viable route')
        
        return best_routes
    
    # TODO: Dyjkstra or MST?
    
    
    

    