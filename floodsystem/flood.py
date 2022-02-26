from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations,tol):
    listStationLevel = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > tol:
            listStationLevel.append((station, station.relative_water_level()))
    return sorted_by_key(listStationLevel, 1, True)

def stations_highest_rel_level(stations,N):
    list_of_highest_rel = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        else:
            
            list_of_highest_rel.append((station, station.relative_water_level()))
    return (sorted_by_key(list_of_highest_rel, 1, True))[:N]

