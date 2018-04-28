import collections
import itertools

from flight_plan.airports import Airport, AirportAtlas

  
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
 
    def add_edge(self, from_vertex, to_vertex): # TODO: from/to_airport not vertex?
        if from_vertex != to_vertex: # no self edges
            self.edges[to_vertex].append(from_vertex)
            self.weights[(from_vertex, to_vertex)] = AirportAtlas.cost_between_airports(from_vertex, to_vertex)
            self.weights[(to_vertex, from_vertex)] = AirportAtlas.cost_between_airports(to_vertex, from_vertex)
 
    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


class Itinerary:

    def __init__(self, airport_list):
        self.airport_list = airport_list
        
    def all_permutations(self): # TODO: limit to perms starting and ending on home
        
        permutations = itertools.permutations(self.airport_list[1:-1])
        
        return list(permutations)
        
    def cheapest_route(self, route_cost_graph): # TODO: cost graph as param of init?
        # TODO: add code to calculate cheapest route via route_cost_graph
        route = [] #FIXME: placeholder
        cost = 0 #FIXME: placeholder
        
        return route, cost
    
    # TODO: shortest route method?
    
    
    

    