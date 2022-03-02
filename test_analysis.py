import matplotlib.dates as date
import numpy as np
from floodsystem.analysis import polyfit

def test_polyfit():
    levels = [216, 125, 64, 27, 16, 1]
    dates = date.num2date([6, 5, 4, 3, 2, 1])
    p=3
    poly, off = polyfit(dates, levels, p)
    assert off ==6
    assert type(poly) != None
    assert len(poly) == 3