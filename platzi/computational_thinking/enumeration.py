def main() -> None:
    goal = int(input('Enter an integer: '))
    answer = 0

    while answer**2 < goal:
        answer += 1

    if answer**2 == goal:
        print(f'The square root of {goal} is {answer}')
    else:
        print(f'{goal} does not have an exact square root')


if __name__ == '__main__':
    main()
