def get_first_program() -> None:
    num_1 = int(input('Enter an integer: '))
    num_2 = int(input('Enter another integer: '))

    if num_1 > num_2:
        print('The first number is greater than the second one')
    elif num_1 < num_2:
        print('The second number is greater than the first one')
    else:
        print('The numbers are equal')


def get_second_program() -> None:
    age_1 = int(input('Enter the age 1 of the person 1: '))
    name_1 = input('Enter the name of the person 1: ')
    age_2 = int(input('Enter the age of the person 2: '))
    name_2 = input('Enter the name of the person 2: ')

    if age_1 > age_2:
        print(f'{name_1} is {age_1 - age_2} years older than {name_2}')
    elif age_1 < age_2:
        print(f'{name_2} is {age_2 - age_1} years older than {name_1}')
    else:
        print(f'{name_1} and {name_2} have the same age')


def main() -> None:
    # First program
    get_first_program()

    # Second program
    get_second_program()


if __name__ == '__main__':
    main()
