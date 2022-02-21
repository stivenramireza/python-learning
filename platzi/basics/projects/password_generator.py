import random


CAPITAL_LETTERS = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
]
LOWERCASE_LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
SYMBOLS = ["!", "#", "$", "&", "/", "(", ")"]
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def generate_password() -> str:
    characters = CAPITAL_LETTERS + LOWERCASE_LETTERS + SYMBOLS + NUMBERS

    password = []
    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)

    generated_password = "".join(password)
    return generated_password


def main() -> None:
    password = generate_password()
    print(f"Your new password is {password}")


if __name__ == "__main__":
    main()
