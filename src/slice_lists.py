planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:]  # planets_after_earth = planets[3:8]
print(planets_after_earth)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort()  # A->Z
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True)  # Z->A
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
