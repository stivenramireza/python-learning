def loop_a_name(name: str) -> None:
    for letter in name:
        print(letter)


def loop_a_phrase(phrase: str) -> None:
    for character in phrase:
        print(character.upper())


def main() -> None:
    # Loop a counter until 1000

    # Using while
    counter = 1
    print(counter)

    while counter < 1000:
        counter += 1
        print(counter)

    # Using for
    for counter in range(1, 1001):
        print(counter)

    # Loop 11 table
    for i in range(0, 10):
        print(f"11*{i} = {11 * i}")

    # Loop a name
    name = input("Enter your name: ")
    loop_a_name(name)

    # Loop a phrase with upper()
    phrase = input("Enter a phrase: ")
    loop_a_phrase(phrase)


if __name__ == "__main__":
    main()
