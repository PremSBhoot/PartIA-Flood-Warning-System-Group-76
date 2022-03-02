from floodsystem.datafetcher import fetch_latest_water_level_data, fetch_station_data
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    #Build Station Input List
    stations_input = build_station_list()
    #set relative water level to output stations with value larger than that
    rel_level = 0.8

    update_water_levels(stations_input)
    #update water levels to current levels
    stations_above_level = stations_level_over_threshold(stations_input, rel_level)
    #get stations above relative water level from own function
    for val in stations_above_level:
        if(val[1]>20):
            continue
            #skip if relative water level is above 20, decided any values
            #above this are outliers - letcombe basset displaying value of 666
            #and has no data points
        
        print(val[0].get_stationName(), val[1])
        #print station name and relative water level (if above threshold)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()