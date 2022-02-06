from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

stations = build_station_list()

print(sorted(inconsistent_typical_range_stations(stations)))