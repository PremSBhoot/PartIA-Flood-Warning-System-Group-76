

from attr import has
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    stations_list = build_station_list()
    coord = (52.2053, 0.1218) 
    stations_sorted_by_distance = stations_by_distance(stations_list, coord)

    assert "Cambridge Jesus Lock" in stations_sorted_by_distance[0][0]
    assert 0.8402364350834995 == stations_sorted_by_distance[0][2]

    

