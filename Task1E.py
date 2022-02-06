from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

stations = build_station_list()
print(rivers_by_station_number(stations,9))
