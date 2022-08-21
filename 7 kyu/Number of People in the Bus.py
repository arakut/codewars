def number(bus_stops):
    arr1 = sum([i[0] for i in bus_stops])
    arr2 = sum([i[1] for i in bus_stops])
    return arr1-arr2
