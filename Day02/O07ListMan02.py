
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.0, 6.5, 7.8, 8.2, 9 + 3j, 10 - 2j, 'eleven', 'twelve', 'thirteen', 'fourteen', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])

print(f"l1 :{l1}")

print("-" * 60)
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("Extend".center(60, "-"))
l1 = list(range(6, 11))
print(F"l1 :{l1}")

l1.extend([11, 12, 13, 14])
print(f"l1 :{l1}")

l1.extend([15])
print(f"l1 :{l1}")

print("insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

