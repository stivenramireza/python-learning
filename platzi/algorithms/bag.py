def bag(bag_lenght: int, weights: list[int], values: list[int], n: int) -> None:
    if n == 0 or bag_lenght == 0:
        return 0

    if weights[n - 1] > bag_lenght:
        return bag(bag_lenght, weights, values, n - 1)

    return max(
        values[n - 1]
        + bag(bag_lenght - weights[n - 1], weights, values, n - 1),
        bag(bag_lenght, weights, values, n - 1),
    )


def main() -> None:
    values = [60, 100, 120]
    weights = [10, 20, 30]
    bag_lenght = 50
    n = len(values)

    result = bag(bag_lenght, weights, values, n)
    print(result)


if __name__ == '__main__':
    main()
