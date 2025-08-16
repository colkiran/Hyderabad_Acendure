
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st :{st}")
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse index
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing with reverse indexes
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1] :{st[::-1]}")

print("-" * 60)
# Strings are immutable
print(f"st :{st}")
print(f'st[0] :{st[0]}')
# st[0] = 'H'

print("-" * 60)
# string Manipulation
st = 'hello world'
print(f"st :{st}")

# replace h with H
res = st.replace("h", "H")
print(f"res :{res}")

print("-" * 60)
res = st.replace("l", "L")
print(f"res :{res}")

print("-" * 60)
res1 = st.replace("l", "L", 1)
print(f"res1 :{res1}")

print("-" * 60)
st = "abc345kdf234x75hyz9078"
# print the numbers from the string
for i in range(0, len(st)):
    if st[i].isnumeric():
        print(st[i], end="")
print()

