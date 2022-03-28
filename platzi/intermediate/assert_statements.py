def divisors(num: int) -> list[int]:
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main() -> None:
    num = input("Enter a number: ")
    assert num.isnumeric(), "You must enter a positive number"
    print(divisors(int(num)))
    print("My program finished")


if __name__ == "__main__":
    main()
