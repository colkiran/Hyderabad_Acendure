
l1 = list(range(1, 11))
print(f"l1 :{l1}")

for i in l1:
    print(i, end=" ")
print()

print('-' * 60)
res = [i for i in l1]
print(res)

print('-' * 60)
l2 = list(range(1, 31))
print(f"l2 :{l2}")

print('-' * 60)
for i in l2:
    if i % 2 == 0:
        print(i, end=" ")
print()

print('-' * 60)
for i in l2:
    if i % 2 == 1:
        print(i, end=" ")
print()

print('-' * 60)
even_num = [i for i in l2 if i % 2 == 0]
print(even_num)

print('-' * 60)
odd_num = [i for i in l2 if i % 2 == 1]
print(odd_num)

print('-' * 60)
squares = [i ** 2 for i in l1]
print(squares)

print('-' * 60)
squares = [i ** 2 for i in range(1, 11)]
print(squares)

print('-' * 60)
l3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1, 2, 3, 4, 5, 6, 7, 8, 9
'''
for i in l3:
    for j in i:
        print(j)
'''

k = [j for i in l3 for j in i]
print(k)
