
print('remove'.center(60, "-"))
l1 = [1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
l1.remove(3)
l1.remove(3)


print(f"l1 :{l1}")
# remove all 2's from the list
# l2=[]
# for i in range(0,len(l1)):
#     if l1[i]!=2:
#         l2.append(l1[i])
# print(l2)

while(l1.count(2)):
    l1.remove(2)

print("-" * 60)
print(f"l1 :{l1}")

print("pop".center(60,"-"))
# pop is the only function that returns the data that was removed from the list

l1 = list(range(1, 11))
print(f"l1 :{l1}")

rem = l1.pop(4)
print(f"rem :{rem}")

rem = l1.pop(2)
print(f"rem :{rem}")

rem = l1.pop(6)
print(f"rem :{rem}")

rem = l1.pop()        # removes the last element from the list
print(f"rem :{rem}")
print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = list(range(1, 21))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
