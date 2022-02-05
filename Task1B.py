from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations_input = build_station_list()
coord = (52.2053, 0.1218) #coordinate of cambridge city centre
stations_sorted_by_distance = stations_by_distance(stations_input, coord)

print(stations_sorted_by_distance[:10])
print(stations_sorted_by_distance[-10:])