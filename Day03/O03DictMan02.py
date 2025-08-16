
print("keys".center(60, "-"))
player = {'name': 'Rahul', 'age': 31, 'runs': 120, 'oppn': 'England', 'venue': 'Lords', 'year': 2003 }
print(f"player :{player}")

print("-" * 60)
k = player.keys()
print(f"k :{k}")

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))


print('values'.center(60, "-"))

player = {'name': 'Rahul', 'age': 31, 'runs': 120, 'oppn': 'England', 'venue': 'Lords', 'year': 2003 }


print(f"player :{player}")

print("-" * 60)
v = player.values()
print(f"values :{v}")

print("get".center(60, "-"))

player = {'name': 'Rahul', 'age': 31, 'runs': 120, 'oppn': 'England', 'venue': 'Lords', 'year': 2003 }

print(f"player :{player}")

print("-" * 60)
print(f"Name  :{player.get('name', 'Invalid key, please enter a valid key')}")
print(f"Venue :{player.get('venui', 'Invalid key, please enter a valid key')}")

print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("setdefault".center(60, "-"))
emp = {'empid': 'EMP101', 'empname': 'Ben', 'Desig': 'MGR'}
print(f"emp :{emp}")

# modify
emp.setdefault('empname', 'John')
emp.setdefault('desig', 'VP')

emp['dob']= '19/03/2000'
emp['dept'] = 'Finance'

print(f"emp :{emp}")

print("pop".center(60, "-"))

player = {'name': 'Rahul', 'age': 31, 'runs': 120, 'oppn': 'England', 'venue': 'Lords', 'year': 2003 }

print(f"player :{player}")

print("-" * 60)
res = player.pop('runs')
print(f"res :{res}")

res = player.pop('oppn')
print(f"res :{res}")

# res = player.pop()
# print(f"res :{res}")

print("-" * 60)
print(f"player :{player}")

print("popitem".center(60, "-"))

player = {'name': 'Rahul', 'age': 31, 'runs': 120, 'oppn': 'England', 'venue': 'Lords', 'year': 2003 }

print(f"player :{player}")

print("-" * 60)

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print("-" * 60)
print(f'player :{player}')
