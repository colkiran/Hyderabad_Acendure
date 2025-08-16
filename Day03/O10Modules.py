
import os
import sys
print(f"All modules in the current Virtual Environment :{os.system('pip list')}")

print('-' * 60)

print(os.getcwd())      # current path

print(os.system("cls"))        # execute any os commands on which python is installed

print(os.cpu_count())          # returns the number of cores in the cpu

print('-' * 60)

number = 10
divisor = 0

try:
    res = number / divisor

except:
    print("Exception caught.....")
    print(sys.exc_info()[0])        # exception class
    print(sys.exc_info()[1])        # message

print('-' * 60)
# environment path - the place where the libraries can be stored
print(sys.path)

print(sys.version)

print(sys.version_info)