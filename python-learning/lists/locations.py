locations = ['nantes','london','singapour','california','dakar']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
locations.append('Montreal')
locations.append('mexico')
locations.append('brazilia')
print('The first three items in the list are:')

for location in locations[1:4]:
    print(location)

print('Three items from the middle of th list are:')

for location in locations[len(locations)//2:]:
    print(location)

print('The last three items on the list are:')

for location in locations[-3:]:
    print(location)
