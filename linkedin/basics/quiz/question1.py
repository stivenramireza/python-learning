def calc(currency: float, *rates) -> None:
    for i in rates:
        print(currency * i)


calc(10.5, 1, 2, 3)
