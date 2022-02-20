#
# Example file for working with conditional statements
#


def main() -> None:
    x, y = 10, 100

    # Conditional flow uses if, elif, else
    if x < y:
        st = 'x is less than y'
    elif x == y:
        st = 'x is the same as y'
    else:
        st = 'x is greater than y'

    print(st)

    # Conditional statement let you use "a if c else b"
    st = 'x is less than y' if x < y else 'x is greater than or the same as y'
    print(st)


if __name__ == '__main__':
    main()
