def check_age(age: int) -> None:
    if age > 17:
        print('You\'re of age')
    else:
        print('You\'re underage')


def check_number(number: int) -> None:
    if number > 5:
        print('It\'s greater than 5')
    elif number == 5:
        print('It\'s equal to 5')
    else:
        print('It\'s less than 5')


def main() -> None:
    age = int(input('Enter your age: '))
    check_age(age)

    number = int(input('Enter a number: '))
    check_number(number)


if __name__ == '__main__':
    main()
