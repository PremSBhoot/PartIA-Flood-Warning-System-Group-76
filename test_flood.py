from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def test_stations_level_over_threshold():
    stations_input = build_station_list()
    rel_level = 0.8
    update_water_levels(stations_input)
    stations_above_level = stations_level_over_threshold(stations_input, rel_level)

    for stations in stations_above_level:
        assert stations[1] > 0.8

def test_stations_highest_rel_level():
    stations_input = build_station_list()
    update_water_levels(stations_input)
    stations_highest_level = stations_highest_rel_level(stations_input,10)
    assert len(stations_highest_level) == 10
    for station in stations_highest_level:
        assert not(station[1] == None)
    assert stations_highest_level[0][1] > stations_highest_level[9][1]
    assert stations_highest_level[0][1] > stations_highest_level[1][1]
    assert len(stations_highest_level) == 10    