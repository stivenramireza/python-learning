from timeit import repeat


def make_repeater_of(n: int) -> object:
    def repeater(word: str) -> object:
        assert isinstance(word, str), 'You must use a string'
        return word * n

    return repeater


def main():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hello'))

    repeat_10 = make_repeater_of(10)
    print(repeat_10('Platzi'))


if __name__ == '__main__':
    main()
