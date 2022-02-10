

from attr import has
from floodsystem.geo import stations_by_distance
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

    print(stations_sorted_by_distance[0][2])
    print(stations_sorted_by_distance[1][2])
    for i in range (len(sublist) - 1):
        print(i)
        assert sublist[i][2] < sublist[i + 1][2]


"""def test_rivers_by_station_number():
    stations_list = build_station_list()
    assert len(rivers_by_station_number()) >= 10
    assert rivers_by_station_number[0][1] >= rivers_by_station_number[9][1]"""


def test_rivers_by_stations_number():
    stations = build_station_list()
    rivers_by_station_numbers = rivers_by_station_number(stations,10)
    assert len(rivers_by_station_numbers) >= 9
    assert rivers_by_station_numbers[0][1] > rivers_by_station_numbers[9][1]     

