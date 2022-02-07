from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations, stations_by_rivers

def run():
    #Build Station Input List
    stations_input = build_station_list()

    #Builds set of all rivers, sorts rivers in asc order, prints length of set (number of rivers) and first 10 rivers
    rivers = rivers_with_stations(stations_input)
    sorted_rivers = sorted(rivers)
    print(len(rivers), "stations. First 10 - ", sorted_rivers[:10])


    #builds dictionary of the stations at each river
    
    stationsOfRivers = stations_by_rivers(stations_input)

    #prints stations of River Aire in asc order
    print("Stations of River Aire")
    print(sorted(stationsOfRivers["River Aire"]))

    #prints stations of River Cam in asc order
    print("Stations of River Cam")
    print(sorted(stationsOfRivers["River Cam"]))

    #prints stations of River Thames in asc order
    print("Stations of River Thames")
    print(sorted(stationsOfRivers["River Thames"]))

if __name__ == "__main__":
        print("*** Task 1D: CUED Part IA Flood Warning System ***")
        run()

