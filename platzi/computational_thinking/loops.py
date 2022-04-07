def get_multiple_loops() -> None:
    internal_counter = 0
    external_counter = 0

    while external_counter < 5:
        while internal_counter < 6:
            print(external_counter, internal_counter)
            internal_counter += 1

            if internal_counter >= 3:
                break

        external_counter += 1
        internal_counter = 0


def get_single_loop() -> None:
    counter = 0

    while counter < 10:
        print(counter)
        counter += 1  # counter = counter + 1


def main() -> None:
    # # Single loop
    # get_single_loop()

    # Multiple loops
    get_multiple_loops()


if __name__ == "__main__":
    main()
