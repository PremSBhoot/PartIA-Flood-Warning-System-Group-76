import datetime
from warnings import catch_warnings
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """build station list"""
    stations_input = build_station_list()
    """update water levels to current values"""
    update_water_levels(stations_input)
    stations_highest = stations_highest_rel_level(stations_input, 10)
    """build a list of 10 stations, will only output 5 - but if there are errors
    in data set for any station we can ignore them and output another, for example
    letcombe basset has no data points, cannot plot or calculate polynomial coefficients"""
    output = 0
    """counter on number of stations plotted"""
    for val in stations_highest:
        dates,levels = fetch_measure_levels(val[0].get_measureID(), datetime.timedelta(days = 2))
        """gets data and levels for stations"""
        if output<5:
            """if less than 5 graphs plotted"""

            """try catch statement, if errors causes throws own error and program doesnt crash
            error caused will be due to polyfit not working due to lack of data from a station"""
            try:
                plot_water_level_with_fit(val[0], dates, levels, 4)
                """uses own function to plot water level and polynomial fit to degree 4 for station"""
                output+=1
            except:
                print("Error, no data available for station", val[0].get_stationName())
                """skips if error - due to lack of data - catches letcombe bassett"""


if __name__ == "__main__":
    print("***Task 2F: CUED Part 1A Flood Warning System")
    run()