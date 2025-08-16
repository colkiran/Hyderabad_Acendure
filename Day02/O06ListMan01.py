
values = list(range(10, 31, 10))
print(f"values :{values}")

# unpack the list
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

# unpack - variable with * can store more than one value
a, b, *c = values
print(a, b, c, sep=", ")

print("-" * 60)
a, *b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]

l3 = [l1, l2]
print(len(l3))
print(f"l3 :{l3}")

print("-" * 60)
# unpack
l4 = [*l1, *l2]
print(len(l4))
print(f"l4 :{l4}")


print("-" * 60)
# enumerate
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter)

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], "\t", letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(index, "\t", letter)

print("-" * 60)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 60)
for lst in mylist:
    print(lst)

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f"Lst({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")
print("-" * 60)

print("-" * 60)
for lst in mylist:
    for num in lst:
        print(num, end=" ")
    print()

print("-" * 60)
l1 = []
print(dir(l1))