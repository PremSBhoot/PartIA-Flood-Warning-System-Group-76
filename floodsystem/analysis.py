import numpy as np
import matplotlib.dates as date

def polyfit(dates,levels,p):
    datesNum=date.date2num(dates)
    t = [val - datesNum[0] for val in datesNum]
    pol= np.polyfit(t, levels, p)
    poly = np.poly1d(pol)
    return poly, datesNum[0]
