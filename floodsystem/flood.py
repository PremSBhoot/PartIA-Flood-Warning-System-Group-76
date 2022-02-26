from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations,tol):
    listStationLevel = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > tol:
            listStationLevel.append((station, station.relative_water_level()))
    return sorted_by_key(listStationLevel, 1, True)