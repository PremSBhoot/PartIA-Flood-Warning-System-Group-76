import matplotlib.pyplot as plt
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib.dates as date

def plot_water_levels(station,dates,levels):
    """plot the list of levels against the list of dates that
    are inputed for the particular station with the axis labelled
    and the title as the station name"""
    plt.plot(dates,levels, color = "black")
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.axhline(y = station.get_typicalRange()[0], color = "green")
    plt.axhline(y = station.get_typicalRange()[1], color = "red")
    plt.title(station.get_stationName())
    plt.legend(["Data levels", "Typical Low", "Typical High"])
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """uses polyfit function to get poly1d object and time shift of x axis
    
    plots dates agains polynomial using polyval to evaljulate polynomial with time (use time shift offset)

    plotes date against actual levels
    plots lines of typical low and high range 
    labels x and y axis accordingly and title with the station name
    uses legend to label lines for niceness

    """
    poly, offset = polyfit(dates,levels, p)
    plt.plot(dates,np.polyval(poly, (date.date2num(dates) - offset)), color='blue')
    plt.plot(date.date2num(dates),levels, color='black')
    plt.axhline(y = station.get_typicalRange()[0], color = "green")
    plt.axhline(y = station.get_typicalRange()[1], color = "red")
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.title(station.get_stationName())
    plt.legend(["Polynomial fit", "Data levels", "Typical Low", "Typical High"])
    plt.show()
