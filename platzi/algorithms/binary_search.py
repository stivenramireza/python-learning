import random


def binary_search(
    searched_list: list[int], start: int, end: int, goal: int
) -> bool:
    if start > end:
        return False

    middle = (start + end) // 2

    if searched_list[middle] == goal:
        return True
    elif searched_list[middle] < goal:
        return binary_search(searched_list, middle + 1, end, goal)
    else:
        return binary_search(searched_list, start, middle - 1, goal)


def main() -> None:
    n = int(input('What\'s the list lenght? '))
    goal = int(input('What number do you want to find? '))

    searched_list = sorted([random.randint(0, 100) for i in range(n)])

    is_found = binary_search(searched_list, 0, len(searched_list), goal)

    print(searched_list)
    print(
        'The element {} {} in the list'.format(
            goal, 'is' if is_found else 'is not'
        )
    )


if __name__ == '__main__':
    main()
