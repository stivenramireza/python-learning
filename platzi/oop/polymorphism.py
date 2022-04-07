class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def advance(self) -> None:
        print("Walking...")


class Cyclist(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def advance(self) -> None:
        print("Riding on my bike...")


def main() -> None:
    person = Person("Stiven")
    person.advance()

    cyclist = Cyclist("Daniel")
    cyclist.advance()


if __name__ == "__main__":
    main()
