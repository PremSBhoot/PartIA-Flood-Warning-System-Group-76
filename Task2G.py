from http.client import CONTINUE
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
import matplotlib.dates as date
import matplotlib.pyplot as plt
import numpy as np


def risk_calculation():
    risk = [] #list of tuples with station and risk (severe, high, moderate, high)
    stations_input = build_station_list()
    update_water_levels(stations_input)
    stationsLevels = stations_level_over_threshold(stations_input, 0)
    p=4
    for val in stationsLevels:
        dates,levels = fetch_measure_levels(val[0].get_measureID(), datetime.timedelta(days = 2))
        if(len(levels)<15):
            print("Insufficient data to complete risk calculation for", val[0].get_stationName())
            continue
       
        poly,offset = polyfit(dates,levels, p)
        derivative = np.polyder(poly)
        dates = (date.date2num(dates)) 
        dates -= offset

        rateOfChange = np.polyval(derivative, dates)
        #plt.plot(dates, np.polyval(poly, dates))
        #plt.plot(dates, rateOfChange)
        #plt.show()
        #print(val[0].get_stationName())
        #print(rateOfChange[0])
        currentRate = rateOfChange[0]
        if((val[1] > 1.6) or (val[1]> 1.3 and currentRate > 1) or (val[1]> 1.1 and currentRate > 2)):
            risk.append((val[0], "Severe"))
            print(val[0].get_stationName(), " Severe")
        elif((val[1] > 1.3) or (val[1]> 1.1 and currentRate > 1) or (val[1]> 1 and currentRate > 2)):
            risk.append((val[0], "High"))
            print(val[0].get_stationName(), " High")
        elif((val[1] > 1.1) or (val[1]> 1 and currentRate > 1) or (val[1]> 0.85 and currentRate > 2)  or (val[1]> 0.8 and currentRate > 2.5) or (val[1]>0.6 and currentRate>3):
            risk.append((val[0], "Moderate"))
            print(val[0].get_stationName(), " Moderate")
        else:
            risk.append((val[0], "Low"))
            print(val[0].get_stationName(), " Low")
    
        

if __name__ == "__main__":
    risk_calculation()