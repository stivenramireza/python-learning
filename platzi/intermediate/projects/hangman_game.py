import os
import random

GAME_DATA = []
INITIAL_ATTEMPTS = 10


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
    return ["_" for i in range(len(word))]


def check_letter_in_word(
    searched_letter: str, correct_word: str, game_word: list[str]
) -> None:
    for i, v in enumerate(correct_word):
        if v == searched_letter:
            game_word[i] = v
        else:
            if v not in game_word:
                game_word[i] = "_"


def start_game() -> None:
    os.system("clear")

    get_game_data()
    assert GAME_DATA
    print(
        f"""
    HANGMAN GAME
    
    You have {INITIAL_ATTEMPTS} attempts
    """
    )

    attempts = 0
    won = False

    index = random.randint(0, len(GAME_DATA))
    correct_word = GAME_DATA[index]
    print(correct_word)
    game_word = draw_initial_line_word(correct_word)

    while attempts < INITIAL_ATTEMPTS:
        drawn_word = " ".join(game_word)
        print(
            f"""
        What's the correct word?
        ------------------------
        {drawn_word}
        """
        )

        letter = input("Enter a letter: ")
        validate_user_input(letter)

        check_letter_in_word(letter, correct_word, game_word)

        user_answer = "".join(game_word)
        if user_answer == correct_word:
            won = True
            break

        attempts += 1
        os.system("clear")

    os.system("clear")
    print("You won!") if won else print(
        f"Game over! The correct word was '{correct_word}'"
    )


def main() -> None:
    start_game()


if __name__ == "__main__":
    main()
