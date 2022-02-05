from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations, stations_by_rivers

stations_input = build_station_list()
rivers = rivers_with_stations(stations_input)
print(len(rivers))

sorted_rivers = sorted(rivers)
print(sorted_rivers[:10])

stationsOfRivers = stations_by_rivers(stations_input)

print(sorted(stationsOfRivers["River Aire"]))
print(sorted(stationsOfRivers["River Cam"]))
print(sorted(stationsOfRivers["River Thames"]))



