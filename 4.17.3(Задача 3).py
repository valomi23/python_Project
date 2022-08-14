
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong' ]
#cities.insert(5, 'and')
massage = f"{','.join(cities[0:5])} and {''.join(cities[5:])}"
print(massage)