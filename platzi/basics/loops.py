LIMIT = 1000000


def main() -> None:
    counter = 0
    power_2 = 2**counter

    while power_2 < LIMIT:
        print(f"2**{counter} is equals to: {power_2}")
        counter += 1
        power_2 = 2**counter


if __name__ == "__main__":
    main()
