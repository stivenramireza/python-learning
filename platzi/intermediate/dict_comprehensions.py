def main() -> None:
    # Without dict comprehensions
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i**3
    print(my_dict)

    # With dict comprehensions
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)


if __name__ == "__main__":
    main()
