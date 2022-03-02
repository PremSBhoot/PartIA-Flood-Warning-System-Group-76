import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels

def run():
    """build station list"""
    stations_input = build_station_list()
    """update water levels to current values"""
    update_water_levels(stations_input)
    """build a list of stations that are relevant in this case"""
    stations_to_use = []
    stations_highest_level = stations_highest_rel_level(stations_input,6)
    """built a list of 6 instead of 5 as station with highest relative water level
    letcombe bassett has no data and should be excluded, can use this in the future if there are similar
    errors with the rest api data"""
    output = 0
    """counter on number of stations plotted"""
    for val in stations_highest_level:
        stations_to_use.append(val[0])
    """over the list built check if data is realistic, if it is use it
    and if not remove it from the list and move to the next item until
    the required number are returned"""
    dates,levels = [],[]
    for station in stations_to_use:
        
        dates,levels = fetch_measure_levels(station.get_measureID(),datetime.timedelta(days=10))
        """get dates and water levels in the past 10 days for the station using measureID"""
        if(len(levels)<20):
            continue
            """there are some outliers such as letcombe bassett which has no data points,
            decided if there are less than 20 data points within the last 10 days to exclude them"""
        plot_water_levels(station,dates,levels)
        """use our function to plot water levels for station"""
        output+=1
        if(output==5):
            """once actually printed 5 graphs - excluding outliers -
             breaks and doesnt print anymore - wont reach this condition but 
             can be used if list is greater and not sure of number of outliers with insufficient
              data in highest relative level list"""
            break

    

if __name__ == "__main__":
    print("***Task 2E: CUED Part 1A Flood Warning System")
    run()
