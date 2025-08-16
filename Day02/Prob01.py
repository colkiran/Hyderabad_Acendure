"""
print the pattern

1
23
456
78910

"""
a=0
for i in range(1,6):
    for j in range(1,i):
        a+=1
        print(a,end="")
    print()
