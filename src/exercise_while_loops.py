new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    input("Enter a planet name,or done if done")

print(planets)
