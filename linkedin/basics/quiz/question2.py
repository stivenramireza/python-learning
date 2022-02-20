a: int = 1
b: int = 2


def func():
    global b
    b = a + b


func()
print(b)
