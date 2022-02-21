def is_prime(number: int) -> bool:
    counter = 0
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
            break
    return counter == 0


def main() -> None:
    number = int(input("Enter a number: "))
    is_prime_number = is_prime(number)
    print("It's prime") if is_prime_number else print("It isn't prime")


if __name__ == "__main__":
    main()
