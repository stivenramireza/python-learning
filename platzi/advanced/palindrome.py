def is_palindrome(word: str) -> bool:
    replaced_word = word.replace(" ", "").lower()
    return replaced_word == word[::-1]


def main():
    palindrome = is_palindrome(100)
    print(palindrome)


if __name__ == "__main__":
    main()
