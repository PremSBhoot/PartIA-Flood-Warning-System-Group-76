import numpy as np
import matplotlib.dates as date

def polyfit(dates,levels,p):

    """function that given the water level time history
    for a station it computes the least squares fit of a polynomial
    to degree p to the water level data
    """


    datesNum=date.date2num(dates)
    """from a list of date time objecs returns list of floats"""
    pol= np.polyfit(datesNum -datesNum[0], levels, p)
    """polyfit using numpy with shjifted x values"""
    poly = np.poly1d(pol)
    """poly1d to get coefficients of polynomial
    
    returns tuple of poly1d object (coefficient) and shift of time
    """
    return (poly, datesNum[0])
    

   
