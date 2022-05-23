# [1, 1, 2, 2, 4] -> [1, 2, 4]


def remove_duplicates(some_list: list[int]) -> None:
    return list(set(some_list))


def main() -> None:
    random_list = [1, 1, 2, 2, 4]
    without_duplicates = remove_duplicates(random_list)
    print(without_duplicates)


if __name__ == '__main__':
    main()
