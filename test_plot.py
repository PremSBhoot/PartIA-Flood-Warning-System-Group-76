
import numpy as np

from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import matplotlib.dates as date

def test_plot_water_levels():
    
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0.5, 1.5)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.set_latestLevel(1)
    y = [0,1,2,3,4,5]
    x = y
    plot_water_levels(s,x,y)
    np.testing.assert_array_equal(y,x)


def test_plot_level_with_fit():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0.5, 1.5)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.set_latestLevel(1)
    levels = [216, 125, 64, 27, 16, 1]
    dates = date.num2date([6, 5, 4, 3, 2, 1])
    p=3
    plot_water_level_with_fit(s, dates, levels, p)
    
