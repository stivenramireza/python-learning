import random


def insertion_sort(sorted_list: list[int]) -> list[int]:
    for i in range(1, len(sorted_list)):
        current_value = sorted_list[i]
        current_position = i
        while (
            current_position > 0
            and sorted_list[current_position - 1] > current_value
        ):  # O(n) * O(n) = O(n*n) = O(n^2)
            sorted_list[current_position] = sorted_list[current_position - 1]
            current_position -= 1
        sorted_list[current_position] = current_value
    return sorted_list


def main() -> None:
    n = int(input('What\'s the list lenght? '))

    started_list = [random.randint(0, 100) for i in range(n)]
    print(started_list)

    sorted_list = insertion_sort(started_list)
    print(sorted_list)


if __name__ == '__main__':
    main()
