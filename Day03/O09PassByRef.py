
def fun(prod):
    print(f"inside the function before :{prod}")
    prod.extend(['fanta', 'tropicana', 'limca'])
    print(f"inside the function after :{prod}")

baverage = ['pepsi', 'coke', 'thumbsup', 'mirinda']

print(f"before the function call :{baverage}")

fun(baverage)

print(f"after the function call :{baverage}")

# refer information and examples on function lambdas


