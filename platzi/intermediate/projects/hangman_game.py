import os
import random

GAME_DATA = []


def get_game_data() -> None:
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        try:
            global GAME_DATA
            GAME_DATA = [word.strip("\n") for word in f]
        except Exception:
            print("Error to read the file")
        finally:
            f.close()


def validate_user_input(letter: str) -> None:
    assert len(letter) == 1, "You must enter a single letter"
    assert letter.isalpha(), "You must enter a letter"


def draw_initial_line_word(word: str) -> None:
    return "_ " * len(word)


def save_temp_answer(answer: str) -> None:
    with open("./files/temp_answer.txt", "w", encoding="utf-8") as f:
        try:
            f.write(answer)
        except Exception:
            print("Error to save the answer")
        finally:
            f.close()


def check_letter_in_word(searched_letter: str, word: str) -> None:
    new_word = ""
    for letter in word:
        if letter == searched_letter:
            new_word += letter
        else:
            new_word += "_ "
    return new_word


def start_game() -> None:
    os.system("clear")

    get_game_data()
    assert GAME_DATA
    print("HANGMAN GAME")

    attempts = 0
    won = False

    index = random.randint(0, len(GAME_DATA))
    correct_word = GAME_DATA[index]
    game_word = draw_initial_line_word(correct_word)

    while attempts < 6:
        print(
            f"""
        What's the correct word?
        ------------------------
        {game_word}
        """
        )

        letter = input("Enter a letter: ")
        validate_user_input(letter)

        new_word = check_letter_in_word(letter, correct_word)

        if new_word == correct_word:
            won = True
            break

        if new_word != game_word:
            game_word = new_word

        attempts += 1
        os.system("clear")

    os.system("clear")
    print("You are the winner!") if won else print(
        f"Game over! The correct word was '{correct_word}'"
    )


def main() -> None:
    start_game()


if __name__ == "__main__":
    main()
