"""
print all prime numbers between 150 and 50, also print the count of prime numbers between them

"""
n=0
for i in range(150,49,-1):
    cntr = 0
    for j in range(2,i):
        if i%j == 0:
           break
    else:
        print(i, end=" ")
        n+=1

print(f"\nthere are {n} prime numbers from 150 to 50")

