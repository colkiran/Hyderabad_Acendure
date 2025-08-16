
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event........")

def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event")


greet()
print("-" * 60)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)
greetGstCty("Rohit")
greetGstCty("Hardik")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
# we can pass arguments to the function in two different ways - args, kwargs
def admsn(name, dob, gender, qlf, city, conno, adrs):
    print(f"Name :{name}")
    print(f"DOB :{dob}")
    print(f"Gender :{gender}")
    print(f"Qualification :{qlf}")
    print(f"city :{city}")
    print(f"Contact No. :{conno}")
    print(f"Address :{adrs}")

# args
admsn("Kevin", '12/05/1989', 'Male', 'M.Tech', 'NYC', '348230493', '5th lane, Sunnyvale')

print("-" * 60)
# kwrgs
admsn(gender='Female', adrs='8th Floor, 10th lane', name='Grace', city='LA', conno='9032492313', dob='09/09/1990', qlf='MS')

print("-" * 60)
# variable length arguments - *args, **kwargs

def ProdNum(*numbers):
    print("*numbers :", *numbers)
    print(f"numbers :{numbers}")
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = ProdNum(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extract_detials(**details):
    print(f"details :{details}")
    print(f"Name :{details['name']}")
    print(f"Age  :{details['age']}")
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)

extract_detials(name='Sachin', age=34, runs=129, oppn="Aus", venue='Perth')

print("-" * 60)
# functions can return values
def multiplyMe(x, y):
    return x * y

print(multiplyMe(4, 7))

# recursive calls - function calling it self
# 1. factorial of a number, 2. fibonacii series

# pass by value and pass by reference
# pass by value - we only pass the data
# pass by reference  - we pass the address along with data


