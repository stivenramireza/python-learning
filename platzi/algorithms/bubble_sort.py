import random


def bubble_sort(sorted_list: list[int]) -> list[int]:
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):  # O(n) * O(n) = O(n*n) = O(n^2)
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list


def main() -> None:
    n = int(input("What's the list lenght? "))

    started_list = [random.randint(0, 100) for i in range(n)]
    print(started_list)

    sorted_list = bubble_sort(started_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
