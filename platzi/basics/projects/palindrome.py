def is_palindrome(word: str) -> bool:
    correct_word = word.replace(" ", "").lower()
    inverse_word = correct_word[::-1]
    return correct_word == inverse_word


def main() -> None:
    word = input("Enter a word: ")
    is_palindrome_word = is_palindrome(word)
    print("It's palindrome") if is_palindrome_word else print("It isn't palindrome")


if __name__ == "__main__":
    main()
