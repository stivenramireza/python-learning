class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def say_hello(self) -> None:
        print(
            'Hello, my name is {} and I am {} years old'.format(
                self.name, self.age
            )
        )


def main() -> None:
    person = Person('Stiven', 23)

    print('Age: {}'.format(person.age))
    person.say_hello()


if __name__ == '__main__':
    main()
