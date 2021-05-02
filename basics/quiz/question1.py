def calc(currency: float, *rates) -> None:
    for i in rates:
        print(currency * i)


def main() -> None:
    calc(10.5, 1, 2, 3)


if __name__ == '__main__':
    main()
