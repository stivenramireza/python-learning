def print_message() -> None:
    print('Special message: ')
    print('I\'m learning to use functions!')


def print_talk(option: int) -> None:
    print('Hello')
    print('How are you going?')
    print('You chose the option %d' % option)
    print('Good bye!')


def sum(a: int, b: int) -> int:
    print('Sum 2 numbers')
    result = a + b
    return result


def main() -> None:
    print_message()
    print_message()
    print_message()

    option = int(input('Choose an option (1, 2, 3): '))

    if option == 1:
        print_talk(option)
    elif option == 2:
        print_talk(option)
    elif option == 3:
        print_talk(option)
    else:
        print('Invalid option')

    result = sum(1, 4)
    print(result)


if __name__ == '__main__':
    main()
