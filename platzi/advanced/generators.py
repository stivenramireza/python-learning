import time


def fibo_gen(max: int = 0) -> int:
    assert max >= 0, 'max must be a positive number'
    n1, n2, counter = 0, 1, 0

    while True:
        match counter:
            case 0:
                yield n1
            case 1:
                yield n2
            case _:
                aux = n1 + n2
                if max in [0, 1] or aux > max:
                    break
                n1, n2 = n2, aux
                yield aux
        counter += 1


def main() -> None:
    fibonacci = fibo_gen(-2)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


if __name__ == '__main__':
    main()
