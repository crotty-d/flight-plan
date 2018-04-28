#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for routes module."""

import pytest
import sys
sys.path.append('.')

from flight_plan.airports import AirportAtlas
from flight_plan.routes import RouteCostGraph, Itinerary

  
# airport_atlas = AirportAtlas.load_data('input/airports.csv')
# 
# g = RouteCostGraph(airport_atlas)
# 
# cheapest_route, route_cost = Itinerary.cheapest_route(g)
