# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from .utils import sorted_by_key  # noqa
    
def stations_by_distance(stations, p):
    return sorted_by_key([(station.get_stationName(), station.get_town(),
    haversine(station.get_coord(), p)) for station in stations], 2, False)

def stations_within_radius(stations, centre, r):
    return [station for station in stations if haversine(station.get_coord(), centre) <= r]

def rivers_with_stations(stations):
    return {station.get_river() for station in stations} #using sets preferable ig

    """rivers = []
    for station in stations:
        if not(station.get_river() in rivers):
            rivers.append(station.get_river())
    return rivers"""
    
def stations_by_rivers(stations):
    dict = {}
    for val in rivers_with_stations(stations):
        stationsOnRiver = []
        for station in stations:
            if val == station.get_river():
                stationsOnRiver.append(station.get_stationName())
        dict.update({val: stationsOnRiver})
    return dict 
