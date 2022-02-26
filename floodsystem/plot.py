import matplotlib.pyplot as plt


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

