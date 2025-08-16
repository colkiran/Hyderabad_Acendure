
print("count".center(60, "-"))
l1 = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2,2 ,2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(60, "-"))

l1 = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2 ,2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(f"l1 :{l1}")

print("-" * 60)
print(f"first 3 :{l1.index(3)}")

print("-" * 60)
print(f"first 3 :{l1.index(3, l1.index(3) + 1)}")

print("-" * 60)
print(f"first 3 :{l1.index(3, l1.index(3, l1.index(3) + 1) + 1)}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# to copy the list l1 to l2
l2 = l1         # shallow copy - sharing the data with address

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
print("=" * 60)

# copy function
l3 = [5, 6, 7, 8, 9]
print(f"l3 before :{l3}")

# copy the list l3 to l4
l4 = l3.copy()          # deep copy - only the data gets copied

print(f"l4 before :{l4}")

l4.extend([10, 11, 12])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
print("=" * 60)

l5 = [10, 20, 30, [1, 2, 3, 4, 5], 40, 50]
print(f"l5 before :{l5}")

# copy the list l5 to l6
l6 = l5.copy()          # deep copy (only for the external array)

print(f"l6 before :{l6}")
l6[3].extend([6, 7, 8, 9])

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
print("=" * 60)

l7 = [5, 10, 15, 20, 25, [2, 4, 6, 8]]
print(f"l7 before :{l7}")

# copy l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 before :{l8}")
l8[-1].extend([10, 12, 14])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

