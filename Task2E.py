import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels

def run():
    stations_input = build_station_list()
    update_water_levels(stations_input)
    stations_to_use = []
    stations_highest_level = stations_highest_rel_level(stations_input,10)
    for val in stations_highest_level:
        stations_to_use.append(val[0])
    dates,levels = [],[]
    for station in stations_to_use:
        dates,levels = fetch_measure_levels(station.get_measureID(),datetime.timedelta(days=10))
        plot_water_levels(station,dates,levels)
    

if __name__ == "__main__":
    print("***Task 2E: CUED Part 1A Flood Warning System")
    run()
