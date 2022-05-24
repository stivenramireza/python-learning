import random


def binary_search_without_recursion(
    data: list[int], target: int, low: int, high: int
) -> bool:
    pass


def binary_search_with_recursion(
    data: list[int], target: int, low: int, high: int
) -> bool:
    if low > high:
        return False

    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search_with_recursion(data, target, low, mid - 1)
    else:
        return binary_search_with_recursion(data, target, mid + 1, high)


def main() -> None:
    data = [random.randint(0, 100) for i in range(10)]
    data.sort()
    print(data)

    target = int(input('What number would you like to find? '))

    found = binary_search_with_recursion(data, target, 0, len(data) - 1)
    print(found)


if __name__ == '__main__':
    main()
