first_planet_input = input('Enter the distance from the sun for the first planet in km')
second_planet_input = input('Enter the distance from the sun for the second planet in km')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = abs(second_planet - first_planet)
print(distance_km)

