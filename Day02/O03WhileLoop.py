
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print()

print("-" * 60)

print(f"After :{i}")

while True:
    print(i, end=" ")
    i -= 1
    if i < 0:
        break