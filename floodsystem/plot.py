import matplotlib.pyplot as plt
import numpy as np
from floodsystem.analysis import polyfit


def plot_water_levels(station,dates,levels):
    x,y = dates,levels
    plt.plot(x,y)
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.axhline(y = station.get_typicalRange()[0])
    plt.axhline(y = station.get_typicalRange()[1])
    plt.title(station.get_stationName())
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, offset = polyfit(dates,levels, p)
    plt.plot(dates,np.polyval(poly, dates) )
    plt.plot(dates,levels)
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
