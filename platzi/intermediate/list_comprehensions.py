def main():
    # Without list comprehensions
    squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)

    print(squares)

    # With list comprehensions
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)


if __name__ == "__main__":
    main()
