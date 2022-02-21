import random


def main() -> None:
    random_number = random.randint(1, 100)
    choosen_number = int(input("Choose a number between 1 and 100: "))

    while choosen_number != random_number:
        if choosen_number < random_number:
            print(f"Choose a number greater than {choosen_number}")
        else:
            print(f"Choose a number less than {choosen_number}")
        choosen_number = int(input("Enter another number: "))
    print("You won!")


if __name__ == "__main__":
    main()
