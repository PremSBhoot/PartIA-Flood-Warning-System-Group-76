from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations_input = build_station_list()
coord = (52.2053, 0.1218) #coordinate of cambridge city centre
stationsWithinRadius = stations_within_radius(stations_input, coord, 10)

print(sorted(station.get_stationName() for station in stationsWithinRadius)) 