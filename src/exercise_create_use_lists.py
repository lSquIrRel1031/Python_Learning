planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)

print(f"There are {len(planets)} planets.")

planets.append("Pluto")
print(f"Actually,there are {len(planets)} planets.")
print(planets[-1], "is the last planet.")