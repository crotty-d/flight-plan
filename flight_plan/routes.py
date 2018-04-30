import os
import csv
import collections
import itertools

  
class RouteGraph:
    """ 
    Mixed multigraph (triple edges) of airports for calculating different itinerary costs.
    
    Three edges connect each pair of nodes (airport code): one undirected edge weighted by great-circle distance,
    and two oppositely directed edges weighted by fuel cost (inter-airport distance * Euro conversion rate).
    These triple edges are simply referred to as edges in the codes.
    """

    def __init__(self, itinerary, airport_atlas):
        """Create instance of RouteCraph object"""
        # Nodes comprise a set of airport codes (initialise as empty set)
        self._nodes = set()

        # Each edge initialised as empty list
        self._edges = collections.defaultdict(list) #TODO: getters methods?
        # Weights initialised as as empty dictionaries
        self._distances = {}
        self._costs = {}
        
        # Airport itinerary and information
        self._itinerary = itinerary
        self._airport_atlas = airport_atlas
        
        # Add nodes and edges to graph based airports in itinerary and data in atlas
        self.build_graph(self._itinerary, self._airport_atlas)
        
        
    def build_graph(self, itinerary, airport_atlas):
        """Add nodes and edges according to airports in itinerary and data in atlas"""
        code_list = itinerary[0:-1]
        for airport_code in code_list:
            self.add_node(airport_code)
        # Add edges between all (unordered) pairs of nodes (airport codes)
        all_node_pairs = list(itertools.combinations(self._nodes, 2))
        for pair in all_node_pairs:
            self.add_edge(*pair)
            
#         for node_i in self._nodes:
#             for node_j in self._nodes:
#                 self.add_edge(node_j, node_i)
        
 
    def add_node(self, airport_code):
        """Add node (airport) to graph."""
        self._nodes.add(airport_code)
        
        
    def airport_euro_rate(self, airport):
        """
        Return the euro exchange rate at the given airport.
        """
        exch_rate = self._airport_atlas.get_euro_rate(airport)
        return exch_rate
 
 
    def add_edge(self, from_node, to_node): # TODO: from/to_airport not node?
        """Add (trilple) edge between two nodes."""
        if from_node != to_node: # no self edges
            self._edges[to_node].append(from_node)
            # Distance weight
            distance = self._airport_atlas.distance_between_airports(from_node, to_node)
            self._distances[(from_node, to_node)] = self._distances[(to_node, from_node)] = distance
            # Cost weights
            exch_rate1 = self._airport_atlas.airport_euro_rate(from_node)
            exch_rate2 = self._airport_atlas.airport_euro_rate(to_node)
            self._costs[(from_node, to_node)] = distance * exch_rate1
            self._costs[(to_node, from_node)] = distance * exch_rate2
            
    
    def get_distance(self, from_node, to_node):
        """Return the distance between two airports as a float."""
        return self._distances[(from_node, to_node)]
    
    
    def get_cost(self, from_node, to_node):
        """Return the (fuel) cost between two airports as a float."""
        return self._costs[(from_node, to_node)]
    
 
    def __str__(self):
        string = "Vertices: " + str(self._nodes) + "\n"
        string += "Edges: " + str(self._edges) + "\n"
        string += "Distances: " + str(self._distances) + "\n"
        string += "Costs: " + str(self._costs) + "\n"

        return string


class Itineraries:
    """...""" #FIXME
    
    _itinerary_list = []

    def __init__(self, itineraries_csv_filepath, airport_atlas, aircraft_dict):
        """
        Create Itineraries object.
        
        Default is empty list.
        Dictionary values must be Airport objects.
        Set csv_filename parameter to construct dictionary from the CSV.
        """
        self.load_data(itineraries_csv_filepath)
        self._airport_atlas = airport_atlas
        self._aircraft_dict = aircraft_dict
    
    
    def load_data(self, itineraries_csv_filepath):
        try:
            with open(itineraries_csv_filepath) as f:
                reader = csv.reader(f)
                for line in reader:
                    itinerary = [field for field in line]
                    self._itinerary_list.append(itinerary)
        except IOError as e:
            print(e)
        
    def get_itinerary_list(self):
        return self._itinerary_list
    
    
    def route_permutations(self): # TODO: limit to perms starting and ending on home
        """
        Get all route permutations for *each* item in itinerary list.
        
        Returns list of permutation lists.
        """
        permutations_for_itineraries = []
        
        for itinerary in self._itinerary_list:
            airport_codes = itinerary[0:-1]
            origin = itinerary[0]
            aircraft_code = itinerary[-1]
            # Get list of all permutations of intermediary airports (exclude origin)
            permutations = list(map(list, itertools.permutations(airport_codes[1:]))) # list and map function to get list of lists
            # Book-end each route list with origin airport to complete routes
            for p in permutations:
                p.insert(0, origin)
                p.append(origin)

            permutations_for_itineraries.append({'airport_codes': airport_codes, 'aircraft': aircraft_code, 'permutations': permutations})     
        
        return permutations_for_itineraries # list of dictionaries
    
        
    def best_routes(self):
        """
        For each itinerary, get cheapest viable route based on the possible permutations.
        
        Returns list of best routes, one for each itinerary.
        """        
        # Go through list of permutations of for each itinerary to find best route
        permutations_for_itineraries = self.route_permutations()
        # Initialise output list of best routes
        best_routes = []
        for route_permutations in permutations_for_itineraries:
            # Create route graph for itinerary
            itinerary = route_permutations['airport_codes']
            print(itinerary)
            route_graph = RouteGraph(itinerary, self._airport_atlas) # list slice to avoid repeated home airport
            print(route_graph.__str__())
            # Aircraft range (limits possible routes)
            aircraft_code = route_permutations['aircraft']
            aircraft_range = self._aircraft_dict.get_aircraft(aircraft_code).get_range()
            print(aircraft_range)
            # Initialise variables; min value as high as possible
            infinity = float('+inf')
            min_route_cost = infinity
            
            # Get cheapest route in itinerary
            best_route = itinerary
            for route in route_permutations['permutations']:
                cost_route = 0
                route_not_viable = False
                # Add up cost of route legs
                for i in range(len(route)-1): # exclude final destination
                    distance_leg = route_graph.get_cost(route[i], route[i+1])
                    print(distance_leg)
                    if distance_leg > aircraft_range:
#                         route_not_viable = True
#                         break
                        pass
                    else:
                        cost_route += route_graph.get_cost(route[i], route[i+1])
                
                if route_not_viable == False and cost_route < min_route_cost:
                    print('best route found')
                    best_route = route
                    min_route_cost = cost_route
                    cost_route = 0 # reset cost counter
            
            # If viable route found, ...
            if min_route_cost:
                # ...assign as best route for that itinerary...
                best_route.append(best_route)
                # ...and add aircraft code...
                best_route.append(aircraft_code)
                # ...and add cost to end of route
                best_route.append(min_route_cost)
            else:
                # ...use input itinerary and add aircraft code and...
                best_route.append(aircraft_code)
                # ...add 'No viable route' to end
                best_route.append('No viable route')
                
            # Add to output list of best routes
            best_routes. append(best_route)
        
        return best_routes
    
    
    
    

    