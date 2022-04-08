from heapq import merge
import random


def merge_sort(sorted_list: list[int]) -> list[int]:
    if len(sorted_list) > 1:
        middle = len(sorted_list) // 2
        left = sorted_list[:middle]
        right = sorted_list[middle:]

        # Recursive call for each middle
        merge_sort(left)
        merge_sort(right)

        # Iterators for the 2 sublists
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list[k] = left[i]
                i += 1
            else:
                sorted_list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            sorted_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sorted_list[k] = right[j]
            j += 1
            k += 1

    return sorted_list


def main() -> None:
    n = int(input("What's the list lenght? "))

    started_list = [random.randint(0, 100) for i in range(n)]
    print(started_list)

    sorted_list = merge_sort(started_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
