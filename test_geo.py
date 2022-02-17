

from attr import has
from floodsystem.geo import rivers_with_stations, stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation


def test_stations_by_distance():
    stations_list = build_station_list()
    coord = (52.2053, 0.1218) 
    stations_sorted_by_distance = stations_by_distance(stations_list, coord)

    assert "Cambridge Jesus Lock" in stations_sorted_by_distance[0][0]
    assert round(stations_sorted_by_distance[0][2] - 0.8402364350834995, 5) == 0.0

    sublist = stations_sorted_by_distance[:10]
    assert len(sublist) == 10

    for i in range (len(sublist) - 1):
        print(i)
        assert sublist[i][2] < sublist[i + 1][2]
    
    assert(type(stations_sorted_by_distance) is list)
    assert(type(stations_sorted_by_distance[0]) is tuple)

def test_stations_within_radius():
    stations_list = build_station_list()
    coord = (52.2053, 0.1218) 
    stationsInRadius = stations_within_radius(stations_list, coord, 10)

    stationNames = []
    for station in stationsInRadius:
        stationNames.append(station.get_stationName())
    
    assert("Bin Brook" in stationNames)
    assert("Cambridge Baits Bite" in stationNames)
    assert("Oakington" in stationNames)


def test_rivers_with_stations():
        stations_list = build_station_list()
        rivers = rivers_with_stations(stations_list)

        assert(len(rivers) >= 950)
        assert("River Thames" in rivers)
        assert("River Severn" in rivers)



def test_rivers_by_stations_number():
    stations = build_station_list()
    rivers_by_station_numbers = rivers_by_station_number(stations,10)
    assert len(rivers_by_station_numbers) >= 9
    assert rivers_by_station_numbers[0][1] > rivers_by_station_numbers[1][1]
    assert rivers_by_station_numbers[1][1] > rivers_by_station_numbers[2][1]
    assert rivers_by_station_numbers[2][1] > rivers_by_station_numbers[5][1]
    assert rivers_by_station_numbers[0][0] == "River Thames"   

