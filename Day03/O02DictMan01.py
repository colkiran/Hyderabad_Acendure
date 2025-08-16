
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print('-' * 60)
d2 = {'name': 'sachin', 'age': 32, 'runs': 87, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print('-' * 60)
d3 = dict([('name', 'rahul'), ('age', 31), ('runs', 120), ('oppn', 'Sri lanka')])
print(f"d3 :{d3}")
print(type(d3))

print('-' * 60)
d4 = dict(name='Sourav', age=30, runs=130, oppn='Bangladesh')
print(f"d4 :{d4}")
print(type(d4))

print('-' * 60)
# CRUD

# create
player = {'name': 'Sachin', 'age': 32, 'runs': 130, 'oppn': 'WI'}
print(f"Player :{player}")

print('-' * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print('-' * 60)
for x in player:
    print(x, "=>", player[x])

print('-' * 60)
# update => modify the existing data, add a new key value pair
player = {'name': 'Sachin', 'age': 32, 'runs': 130, 'oppn': 'WI'}
print(f"Player :{player}")

# adding new key value
player['venue'] = 'Sabina Park'
player['year'] = '2003'

# modifying the existing key value
player['name'] = 'Tendulkar'
player['runs'] = 165

print(f"player :{player}")

print('-' * 60)
# Deleting
print(f"player :{player}")
# del is not a function, it's a keyword
del player['age']
del player['year']

print(f"player :{player}")

print('-' * 60)
print(dir(player))
