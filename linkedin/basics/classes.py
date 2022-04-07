#
# Example file for working with classes
#


class MyClass:
    def method1(self) -> None:
        print("MyClass method1")

    def method2(self, some_string: str) -> None:
        print(f"MyClass method2: {some_string}")


class AnotherClass(MyClass):
    def method1(self) -> None:
        MyClass.method1(self)
        print("AnotherClass method1")

    def method2(self, some_string: str) -> None:
        print(f"AnotherClass method2")


def main() -> None:
    c1 = MyClass()
    c1.method1()
    c1.method2("This is a string")

    c2 = AnotherClass()
    c2.method1()
    c2.method2("This is a string")


if __name__ == "__main__":
    main()
