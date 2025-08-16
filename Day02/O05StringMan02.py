"""
maketrans => convert the string byte by byte => replace all 'a' with 'z'
translate
"""
print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")
# length of a and b should be the same
a = 'helowrd'
b = 'HELOWRD'
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(res)

print("format".center(60, "-"))
print("Welcome {}, what a {} player".format("Sachin", "class"))

print("Welcome {name} with a rating {rat} what a {adj} player for {ctry}".format(ctry = 'India', adj = 'superb', rat=4.5, name='Sachin'))

print("Welcome {name} with a rating {rat:.2f} what a {adj} player for {ctry}".format(ctry = 'India', adj = 'superb', rat=4.5789739, name='Sachin'))

print("-" * 60)
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!a} {val!r}".format(val="A"))
print("{num} {num} {num}".format(num = 36))
print("{num:10} {num:b} {num:f}".format(num = 36))

print("-" * 60)
# alignment
print("{num:15} Tendulkar".format(num=36))
print("{num:15} Tendulkar".format(num="Sachin"))

print("-" * 60)
print("{num:>15} Tendulkar".format(num="Sachin"))         # right
print("{num:^15} Tendulkar".format(num="Sachin"))         # Center
print("{num:<15} Tendulkar".format(num="Sachin"))         # Center

print("-" * 60)
print("{num:5}".format(num=23648236487632))
print("{num:15}".format(num=450))
print("{num:015}".format(num=450))

print("-" * 60)
print("{num:25}".format(num="Sachin Tendulkar"))
print("{num:.6}".format(num="Sachin Tendulkar"))
print("{num:-^60}".format(num="Python"))

print("Python".center(60, "-"))