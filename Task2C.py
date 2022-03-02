from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """build station list"""
    stations_input = build_station_list()
    """update the water levels to their current values"""
    update_water_levels(stations_input)
    """use the relative level function to build a list of N stations with
    the highest relatiev water levels"""
    stations_highest_level = stations_highest_rel_level(stations_input,11)
    output=0
    """check there is realistic data for all stations in the list, if there
    is not the station will be removed from the list until a list of the 
    chosen length can be returned"""
    for val in stations_highest_level:
        if(val[1] > 20):
            continue
        print(val[0].get_stationName(), val[1])
        output+=1
        if(output ==10):
            break
        


if __name__ == "__main__":
    print("***Task 2C: CUED Part 1A Flood Warning System")
    run()