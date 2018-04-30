# -*- coding: utf-8 -*-

import csv
import collections
import itertools

  
class RouteGraph:
    """ 
    Directed multigraph (double edges) of airports for calculating different itinerary costs.
    
    Two doubly weighted edges connect each pair of nodes (airport codes): Each is symmetrically weighted (~undirected) by great-circle distance,
    and asymmetrically weighted (~directed) by fuel cost (inter-airport distance * Euro conversion rate).
    """

    def __init__(self, itinerary, airport_atlas):
        """Create instance of RouteCraph object"""
        # Nodes comprise a set of airport codes (initialise as empty set)
        self._nodes = set()

        # Each edge initialised as empty list
        self._edges = collections.defaultdict(list)
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
        code_list = itinerary
        for airport_code in code_list:
            self.add_node(airport_code)
        # Add edges between all nodes (airport codes)
        for node_i in self._nodes:
            for node_j in self._nodes:
                self.add_edge(node_j, node_i)
        
 
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
        """Add edge between two nodes."""
        if from_node != to_node: # no self edges
            self._edges[to_node].append(from_node)
            # Distance weight
            distance = self._airport_atlas.distance_between_airports(from_node, to_node)
            self._distances[(from_node, to_node)] = distance
            # Cost weights
            exch_rate = self._airport_atlas.airport_euro_rate(from_node)
            self._costs[(from_node, to_node)] = distance * exch_rate
            
    
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
    _best_routes = []

    def __init__(self, itineraries_csv_filepath, airport_atlas, aircraft_dict, outut_csv_path='/home/d/Git/flight_plan/flight_plan/output/bestroutes.csv'):
        """
        Create Itineraries object.
        
        Default is empty list.
        Dictionary values must be Airport objects.
        Set csv_filename parameter to construct dictionary from the CSV.
        """
        self.load_data(itineraries_csv_filepath)
        self._airport_atlas = airport_atlas
        self._aircraft_dict = aircraft_dict
        self._outut_csv_path = outut_csv_path
        self._best_routes = []
    
    
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
        for route_permutations in permutations_for_itineraries:
            # Create route graph for itinerary
            itinerary = route_permutations['airport_codes']
            print(itinerary)
            route_graph = RouteGraph(itinerary, self._airport_atlas) # list slice to avoid repeated home airport
            
            # Aircraft range (limits possible routes)
            aircraft_code = route_permutations['aircraft']
            aircraft_range = self._aircraft_dict.get_aircraft(aircraft_code).get_range()
            print('Aircraft range: ', aircraft_range)
            
            # Initialise variables; min value as high as possible
            infinity = float('+inf')
            min_route_cost = infinity
            
            # Get best (cheapest) route in itinerary
            best_route = itinerary # initalise best route as order given in input file
            best_route.append(itinerary[0]) # make round trip
            for route in route_permutations['permutations']:
                cost_route = 0
                route_not_viable = False
                # Sum cost of route legs
                for i in range(len(route)-1):
                    distance_leg = route_graph.get_cost(route[i], route[i+1])
                    if distance_leg > aircraft_range:
                        print('Out of range: route not viable')
                        route_not_viable = True
                        break
                    else:
                        cost_route += route_graph.get_cost(route[i], route[i+1])
                
                if not route_not_viable and cost_route < min_route_cost:
                    print('New best route found. Cost: ', cost_route)
                    best_route = route
                    min_route_cost = cost_route
                    cost_route = 0 # reset cost counter
            
            # If viable route found, ...
            if min_route_cost < infinity:
                # ...and add aircraft code...
                best_route.append(aircraft_code)
                # ...and add cost to end of route
                best_route.append(min_route_cost)
            else:
                # If not, just add input itinerary and add aircraft code and...
                best_route.append(aircraft_code)
                # ...add 'No viable route' to end
                best_route.append('No viable route')
                
            # Add to output list of best routes
            self._best_routes.append(best_route)
        
        # Display best routes in terminal
        print('\n-------------\nBEST ROUTES\n-------------')
        for route in self._best_routes:
            print(route)
            
        return self._best_routes
    
    
    def routes_to_csv(self):
        """
        Output best routes to CSV file.
        
        Note: Run best_routes method first; otherwise no best routes will have
        been calculated and the file will be empty.
        """
        try:
            with open(self._outut_csv_path, 'w') as f:
                writer = csv.writer(f)
                for route in self._best_routes:
                    writer.writerow(route)
            print('CSV saved as', self._outut_csv_path)
        except IOError as e:
                print(e)
    
    
    

    