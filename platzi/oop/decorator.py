def decorated_function(function: object) -> object:
    def wrapper():
        print("This is the last message...")
        function()
        print("This is the first message...")

    return wrapper


@decorated_function
def buzz() -> None:
    print("Buzzzzzz")


def main() -> None:
    buzz()


if __name__ == "__main__":
    main()
