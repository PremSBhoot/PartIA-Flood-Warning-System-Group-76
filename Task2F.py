import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations_input = build_station_list()
    update_water_levels(stations_input)
    stations_highest_5 = stations_highest_rel_level(stations_input, 5)
    for val in stations_highest_5:
        dates,levels = fetch_measure_levels(val[0].get_measureID(), datetime.timedelta(days = 2))
        plot_water_level_with_fit(val[0], dates, levels, 4)
if __name__ == "__main__":
    print("***Task 2F: CUED Part 1A Flood Warning System")
    run()