from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
def run():
    #Build Station Input List
    stations_input = build_station_list()

    #coordinate of cambridge city centre
    coord = (52.2053, 0.1218) 

    #retrives stations within radius of 10 from coordinate
    stationsWithinRadius = stations_within_radius(stations_input, coord, 10)

    print("Prints sorted list in ascending order of stations within the radius")
    print(sorted(station.get_stationName() for station in stationsWithinRadius)) 

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()