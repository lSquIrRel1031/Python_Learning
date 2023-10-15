planet = {
    'name': 'Earth',
    'moons': 1
}

# get
print(planet['name'])  # print(planet.get('name'))

planet['name'] = 'MakeMake'  # planet.update({'name': 'MakeMake'})

# add

# planet.update({
#    'name': 'Jupiter',
#    'moons': 79
# })
planet['name'] = 'Jupiter'
planet['moons'] = 79

# create & delete keys
planet['orbit period'] = 4333

planet.pop('orbit period')

# complex ones
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
