# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    #added getter methods for encapsulation - public interface to access private data 
    def get_stationName(self):
        return self.name
    def get_stationID(self):
        return self.station_id
    def get_measureID(self):
        return self.measure_id
    def get_coord(self):
        return self.coord
    def get_town(self):
        return self.town
    def get_river(self):
        return self.river
    def get_typicalRange(self):
        return self.typical_range
    def set_latestLevel(self, val):
        self.latest_level = val
    def set_typicalRange(self, val):
        self.typical_range = val
        
    def typical_range_stations(self):
        """function to check if typical range has a value or if the upper limit is lower than 
        the lower limit"""
        return not(self.typical_range == None or self.typical_range[1] < self.typical_range[0])

    def relative_water_level(self):
        """
        function to calculate relative water level,
        if there is no current value for level at station or
        typical range is inconsistent, return none
        
        else return the relative water level, formula to be seen in code.."""
        if(self.latest_level == None or not(self.typical_range_stations())):
            return None
        else:
            return((self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0]))

        
def inconsistent_typical_range_stations(stations):
   """function that itterates stations through typical_range_stations and creates a
   list of all stations that are returned"""
   stations_inconsistent = []
   for station in stations:
       if not(station.typical_range_stations()):
           stations_inconsistent.append(station.get_stationName())
   return stations_inconsistent

   


