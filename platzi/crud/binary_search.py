import random


def binary_search_without_recursion(data: list[int], target: int) -> bool:
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


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

    # # With recursion
    found = binary_search_with_recursion(data, target, 0, len(data) - 1)
    print(found)

    # Without recursion
    found = binary_search_without_recursion(data, target)
    print(found)


if __name__ == '__main__':
    main()
