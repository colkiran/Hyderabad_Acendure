
for i in range(1, 11):
    print(i, end=" ")
print()    # to print a newline

# print("hello world")
print("-" * 60)

for i in range(1, 31, 2):
    print(i, end=" ")

print("-" * 60)

for i in range(1, 31):
    if i % 2 == 0:
        print(i, end=" ")

print("-" * 60)

for i in range(15, 0, -1):
    print(i, end=" ")

print("-" * 60)

for i in range(1, 31, 1):
    # if i > 24:
    #     break           # stop the current iteration
    if i % 2 == 1:
        continue        # skip the current iteration
    print(i, end=" ")
else:
    print("\nCompleted iterating numbers.....")