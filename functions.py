#
# Example file for working with functions
#

# Define a basic function
def func1() -> None:
    print('I am a function')

# Function that takes arguments
def func2(arg1: int, arg2: int) -> None:
    print(arg1, ' ', arg2)

# Function that returns a value
def cube(x: int) -> int:
    return x * x * x

# Function with default value for an argument
def power(num: int, x: int = 1) -> int:
    result: int = 1
    for i in range(x):
        result = result * num
    return result

# Function with variable number of arguments
def multi_add(*args) -> int:
    result: int = 0
    for x in args:
        result = result + x
    return result

func1()
print(func1())
print(func1)

func2(10, 20)
print(func2(10, 20))
print(cube(3))

print(power(2))
print(power(2, 3))
print(power(x=3, num=2))

print(multi_add(10, 4, 5, 10, 4))
