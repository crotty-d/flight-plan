#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for routes module."""

import pytest
import sys
sys.path.append('.')

from flight_plan.airports import AirportAtlas
from flight_plan.aircraft import AircraftDictionary
from flight_plan.currencies import CountryCurrencyCodes, EuroRates
from flight_plan.routes import RouteGraph, Itineraries


# Store airport data in AirportAtlas object
atlas = AirportAtlas(csv_filename='airport.csv')
# Store aircraft data in AircraftDictionary object
aircraft_dict = AircraftDictionary(csv_filename='aircraft.csv')
# Store countries' currency codes CountryCurrencyCodes object
currency_codes = CountryCurrencyCodes(csv_filename='countrycurrency.csv')
# Store euro exchange rates for all currency codes (from euro to currency) in EuroRate object
euro_rates = EuroRates(csv_filename='currencyrates.csv')

route_graph = RouteGraph().bulid_from_atlas(atlas)

# def distance_between_airports(airport_code1, airport_code2):
#     """
#     Return the distance between two airports as a float.
#     """
#     airport1 = airport_code1
#     airport2 = airport_code2
#     
#     return airport2
# 
distance = atlas.distance_between_airports('DUB', 'JFK')
print(distance)

# route_graph.add_edge('DUB', 'JFK')
# # route_graph.bulid_from_atlas(atlas)
# cost = route_graph.get_cost('DUB', 'JFK')
# print(cost)

import itertools
import numpy as np
code_list = np.array(atlas.get_code_list())
print(code_list)
all_node_pairs = list(itertools.combinations(code_list, 2))
# for pair in all_node_pairs:
#     print(pair)
print('finished')
 
print(*all_node_pairs[1003])


# airport_atlas = AirportAtlas.load_data('input/airports.csv')
# 
# g = RouteCostGraph(airport_atlas)
# 
# cheapest_route, route_cost = Itinerary.cheapest_route(g)
