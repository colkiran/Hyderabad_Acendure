
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3.5, 4.0, 'five', 'six', 7 + 2j, 8 - 5j, True, False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(10, 101, 10))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
t5 = 10, 20, 30, 40, 50
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
#TUPLES ARE IMMUTABLE
t1 = tuple(range(1, 6))
print(f"t1 :{t1}")
# t1[0] = 100
# print(f"t1[0] :{t1[0]}")

print("-" * 60)
# print(dir(t1))
# count, index

print("count".center(60, "-"))
t1 = (1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1 ,1 ,1, 1)
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
print(f"1 :{t1.count(1)}")
print(f"2 :{t1.count(2)}")
print(f"3 :{t1.count(3)}")
print(f"6 :{t1.count(6)}")

print("index".center(60, "-"))

t1 = (1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1 ,1 ,1, 1)
print(f"t1 :{t1}")

print(f"first 3 :{t1.index(3)}")
print(f"second 3 :{t1.index(3, t1.index(3) + 1)}")
print(f"Third 3 :{t1.index(3, t1.index(3, t1.index(3) + 1) + 1)}")

