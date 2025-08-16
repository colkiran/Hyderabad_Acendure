# numbers and strings are immutable
# in python full accessibility means to change the value of the variable

def fun(x):
    print(f"value of x inside before :{x}")
    x += 500
    print(f"value of x inside after :{x}")

n = 10

print(f"n before function call :{n}")

fun(n)

print(f"n before function call :{n}")
