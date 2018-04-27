import collections
import math
import itertools

from airports import Airport, AirportAtlas
 
 
# class RouteDistanceGraph:
#     """ 
#     Undirected graph of airports for calculating different itinerary distances.
#     
#     Weighted by inter-airport distance.
#     """
# 
#     def __init__(self):
#         self.vertices = set()
# 
#         # makes the default value for all vertices an empty list
#         self.edges = collections.defaultdict(list)
#         self.weights = {}
#  
#     def add_vertex(self, value):
#         self.vertices.add(value)
#  
#     def add_edge(self, from_vertex, to_vertex, distance):
#         if from_vertex != to_vertex: # no self edges
#             self.edges[from_vertex].append(to_vertex)
#             self.edges[to_vertex].append(from_vertex) # undirected graph
#             self.weights[(from_vertex, to_vertex)] = distance
#             self.weights[(to_vertex, from_vertex)] = distance # undirected graph
#  
#     def __str__(self):
#         string = "Vertices: " + str(self.vertices) + "\n"
#         string += "Edges: " + str(self.edges) + "\n"
#         string += "Weights: " + str(self.weights)
#         return string
#     
    
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


class itinerary:

    def __init__(self, airport_list):
        self.airport_list = airport_list
        
    def all_permutations(self): # TODO: limit to perms starting and ending on home
        itertools.permutations(self.airport_list)
        
    def cheapest_route(self, route_cost_graph):
        # TODO: add code
        pass
    
 

def dijkstra(graph, start):
    # initializations
    S = set()

    # delta represents the length shortest distance paths from start -> v, for v in delta.
    # We initialize it so that every vertex has a path of infinity
    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)

    # then we set the path length of the start vertex to 0
    delta[start] = 0

    # while there exists a vertex v not in S
    while S != graph.vertices:
        # let v be the closest vertex that has not been visited...it will begin at 'start'
        v = min((set(delta.keys()) - S), key=delta.get)

        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v,neighbor]

            # is the new path from neighbor through
            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path

                # set the previous vertex of neighbor to v
                previous[neighbor] = v
        S.add(v)

    return (delta, previous)
 
 
 
def shortest_path(graph, start, end):
    """
    Uses dijkstra function in order to output the shortest path from start to end
    """
    delta, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path
  
  
if __name__ == "__main__":
    
    airport_atlas = AirportAtlas.loadData('input/airports.csv')
    
    g = RouteCostGraph(airport_atlas)

    #     vertex a adjacency list
    g.add_edge('a', 'b', 4)
    g.add_edge('a', 'c', 6)
    g.add_edge('a', 'd', 7)
    g.add_edge('a', 'e', 5)
    g.add_edge('a', 'j', 1)
    #     vertex b adjacency list
    g.add_edge('b', 'e', 9)
    g.add_edge('b', 'f', 8)

    g.add_edge('c', 'd', 2)

    g.add_edge('d', 'j', 3)

    g.add_edge('e', 'f', 4)
    g.add_edge('e', 'h', 3)

    g.add_edge('f', 'g', 7)

    g.add_edge('g', 'i', 15)

    g.add_edge('h', 'i', 12)
    g.add_edge('i', 'j', 9)
    print("graph: ", g)
    print(dijkstra(g, 'c'))

    print(shortest_path(g, 'c', 'g'))