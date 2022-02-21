def main() -> None:
    # Loop only pair numbers
    for counter in range(1000):
        if counter % 2 != 0:
            continue
        print(counter)

    # Loop until 5678 is present
    for i in range(10000):
        print(i)
        if i == 5678:
            break

    # Loop until letter is o
    text = input("Enter a text: ")
    for letter in text:
        if letter == "o":
            break
        print(letter)

    # Loop only odd numbers
    counter = 0

    while counter < 1000:
        counter += 1
        if counter % 2 == 0:
            continue
        print(counter)

    # Loop until 5678 is present
    counter = 0
    while counter < 10000:
        counter += 1
        print(counter)
        if counter == 5678:
            break


if __name__ == "__main__":
    main()
