from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    #Build Station Input List
    stations_input = build_station_list()

    #coordinate of cambridge city centre
    coord = (52.2053, 0.1218) 
    stations_sorted_by_distance = stations_by_distance(stations_input, coord)

    #print 10 closest stations from coordinate specified
    print("10 closest stations from ", coord)
    print(stations_sorted_by_distance[:10])

    #print 19 furthest stations from coordinate specified
    print("10 furthest stations from ", coord)
    print(stations_sorted_by_distance[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()