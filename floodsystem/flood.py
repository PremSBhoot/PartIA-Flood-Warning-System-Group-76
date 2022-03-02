from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations,tol):
    """creates empty list,
    if thjere is no data for water level, skips, if the
    water level is above the threshold, add the station object
    and the relative water level to the list

    return list sorted by relative water level descending order
    """
    listStationLevel = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > tol:
            listStationLevel.append((station, station.relative_water_level()))
    return sorted_by_key(listStationLevel, 1, True)

def stations_highest_rel_level(stations,N):
    """build list empty ready to fill"""
    list_of_highest_rel = []
    for station in stations:
        """loop over stations, if there is no data pass over it
        if there is it will be added to the list created in the 
        previous lines"""
        if station.relative_water_level() == None:
            continue
        else: 
            list_of_highest_rel.append((station, station.relative_water_level()))
    return (sorted_by_key(list_of_highest_rel, 1, True))[:N]

