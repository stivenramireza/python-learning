class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_distance(self, coordinate: object) -> float:
        try:
            x_diff = (self.x - coordinate.x) ** 2
            y_diff = (self.y - coordinate.y) ** 2
            distance = (x_diff + y_diff) ** 0.5
            return round(distance, 2)
        except TypeError:
            return 0


def main():
    coordinate_1 = Coordinate(3, 30)
    coordinate_2 = Coordinate(4, 8)

    distance = coordinate_1.get_distance(coordinate_2)
    print(distance)


if __name__ == '__main__':
    main()
