def inc(a: int, b: int = 1) -> int:
    return a + b


a = inc(1)  # 2
a = inc(a, a)  # 4
print(a)  # 4
