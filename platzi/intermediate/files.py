def read() -> None:
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write() -> None:
    names = ['Stiven', 'Miguel', 'Pepe', 'Christian', 'Rocío']
    with open('./files/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def main() -> None:
    write()


if __name__ == '__main__':
    main()
