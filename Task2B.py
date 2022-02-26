from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    #Build Station Input List
    stations_input = build_station_list()
    rel_level = 0.8

    update_water_levels(stations_input)
    stations_above_level = stations_level_over_threshold(stations_input, rel_level)
    for val in stations_above_level:
        print(val[0].get_stationName(), val[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()