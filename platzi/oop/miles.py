class Miles:
    def __init__(self, distance: float = 0) -> None:
        self._distance = distance

    def convert_to_kilometers(self) -> float:
        return self._distance * 1.609344

    @property
    def distance(self) -> float:
        print('Getter method')
        return self._distance

    @distance.setter
    def distance(self, distance: float) -> None:
        if distance < 0:
            raise ValueError(
                'It is not possible to convert distances less than 0'
            )
        print('Setter method')
        self._distance = distance


def main() -> None:
    airplane = Miles()
    airplane.distance = 200
    print(airplane.distance)


if __name__ == '__main__':
    main()
