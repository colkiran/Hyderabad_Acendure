
print("items".center(60, "-"))
# items is a combination of keys and values

emp = {
    'emp1': {'empid': 'EMP111', 'ename': 'Jack', 'gender': 'male', 'dob': '13/04/1997', 'desig': 'MGR', 'salary': 145000},
    'emp2': {'empid': 'EMP202', 'ename': 'Tina', 'gender': 'female', 'dob': '13/04/2002', 'desig': 'TL',  'salary': 85000},
    'emp3': {'empid': 'EMP330', 'ename': 'Mike', 'gender': 'male', 'dob': '13/04/1993', 'desig': 'GM', 'salary': 165000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("update".center(60, "-"))
emp1 = {'empid': 'EMP111', 'ename': 'Jack', 'gender': 'male', 'salary': 145000}
print(f"emp1 :{emp1}")
print(type(emp1))

print("-" * 60)
emp2 =  {'empid': 'EMP202', 'ename': 'Tina', 'dob': '13/04/2002', 'desig': 'TL'}
print(f"emp2 :{emp2}")
print(type(emp2))
# update emp1 with emp2's values

print("-" * 60)
emp1.update(emp2)

print(f"emp1 :{emp1}")

print("copy".center(60, "-"))
# emp1 = {'empid': 'EMP111', 'ename': 'Jack', 'gender': 'male', 'salary': 145000,
#         'desig' :{'hp': 'SE', 'tcs': 'Sr. SE', 'genpact': 'TL'}}
emp1 = {'empid': 'EMP111', 'ename': 'Jack', 'gender': 'male', 'salary': 145000}
print(f"emp1 before :{emp1}")

# copy emp1 to emp2
emp2 = emp1             # shallow copy - sharing the data with address

print(f"emp2 before :{emp2}")

emp2['dept'] = 'Finance'
emp2['desig'] = 'MGR'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("-" * 60)
print("-" * 60)

emp3 = {'empid': 'EMP202', 'ename': 'Tina', 'dob': '13/04/2002', 'desig': 'TL'}
print(f"emp3 before :{emp3}")

# copy emp3 to emp4
emp4  = emp3.copy()         # deep copy - only the data gets shared
print(f"emp4 before :{emp4}")

emp4['dept'] = 'MKT'
emp4['salary'] = 95000

print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("-" * 60)
print("-" * 60)

emp5 = {'empid': 'EMP111', 'ename': 'Jack', 'gender': 'male', 'salary': 145000,
        'desig' :{'hp': 'SE', 'tcs': 'Sr. SE', 'genpact': 'TL'}}
print(f"emp5 before :{emp5}")

# copy emp5 to emp6
emp6 = emp5.copy()          # deep copy

print(f"emp6 before :{emp6}")

emp6['desig']['IBM'] = 'TM'
emp6['desig']['CTS'] = 'MGR'

print(f"emp6 after :{emp6}")
print(f'emp5 after :{emp5}')

print("-" * 60)
print("-" * 60)

emp7 = {'empid': 'EMP111', 'ename': 'Jack', 'gender': 'male', 'salary': 145000,
        'desig' :{'hp': 'SE', 'tcs': 'Sr. SE', 'genpact': 'TL'}}

print(f"emp7 before :{emp7}")

# copy emp7 to emp8
from copy import deepcopy
emp8 = deepcopy(emp7)          # deep copy

print(f"emp8 before :{emp8}")

emp8['desig']['IBM'] = 'TM'
emp8['desig']['CTS'] = 'MGR'

print(f"emp8 after :{emp8}")
print(f'emp7 after :{emp7}')

