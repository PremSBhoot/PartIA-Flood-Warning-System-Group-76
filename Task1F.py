from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations



def run():
    """build a list of stations"""
    stations = build_station_list()
    """build a list of stations with inconsistent data using 
    inconsistent_typical_range_stations"""
    print(sorted(inconsistent_typical_range_stations(stations)))
if __name__ == "__main__":
    print("***Task 1E: CUED Part 1A Flood Warning System")
    run()
