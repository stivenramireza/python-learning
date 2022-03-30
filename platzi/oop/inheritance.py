class Rectangle:

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return self.base * self.height


class Square(Rectangle):

    def __init__(self, side: float) -> None:
        super().__init__(side, side)


def main() -> None:
    rectangle = Rectangle(base=3, height=4)
    print(rectangle.get_area())

    square = Square(5)
    print(square.get_area())


if __name__ == "__main__":
    main()
