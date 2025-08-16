
"""
1. int
2. float
3. complex
"""

a = 10
b = -10

print(f"a :{a}")        # interpolation
print(type(a))          # RTTI - Run Time Type Identification
print(f"b :{b}")
print(type(b))

print("-" * 60)

c = 10.9
d = -10.9
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = 2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3.3j
h = -5.3j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print("max :", max([1, 8, 4, 7, 9, 6, 3]))
print("min :", min([1, 8, 4, 7, 9, 6, 3]))

print("-" * 60)
z = 2 + 3.5
print(f"z :{z}")
print(type(z))

print("-" * 60)
x = 2
y = 3.5
z = x + y
print(f"x :{type(x)}")
print(f"y :{type(y)}")
print(f"z :{type(z)}")

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11   :{11}")          # decimal
print(f"0b11 :{0b11}")
print(f"0b101 :{0b101}")
print(f"0o11 :{0o11}")
print(f"0o111 :{0o111}")
print(f"0xe   :{0xe}")
print(f"0xa   :{0xa}")

print("Number System Conversion".center(60, "-"))
a = 100
print(f"a :{a}")
print(f"bin(a) :{bin(a)}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
