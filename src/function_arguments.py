def distance_from_earth(destination):
    if destination == 'Moon':
        return 238855
    else:
        return "Unable to compute to the destination"


distance_moon = float(distance_from_earth('Moon'))


def days_to_complete(distance, speed):
    hours = distance / speed
    return hours / 24


print(days_to_complete(distance_moon, 75))
