# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
<<<<<<< HEAD
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

=======
>>>>>>> c8298b505b2a06406df237498e849fd6a272a9e9

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
<<<<<<< HEAD
    stations = build_station_list()
    list_of_inconsistent = inconsistent_typical_range_stations(stations)
    assert len(list_of_inconsistent) == 28



=======
    assert len(inconsistent_typical_range_stations) >= 1
>>>>>>> c8298b505b2a06406df237498e849fd6a272a9e9
