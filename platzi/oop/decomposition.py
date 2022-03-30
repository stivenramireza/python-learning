class Car:
    def __init__(self, model: str, brand: str, color: str) -> None:
        self.model = model
        self.brand = brand
        self.color = color
        self._status = "resting"
        self._motor = Motor(cylinders=4)

    def accelerate(self, acceleration_type: str = "slow") -> None:
        if acceleration_type == "fast":
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)

        self._status = "moving"


class Motor:
    def __init__(self, cylinders: int, motor_type: str = "gasoline") -> None:
        self.cylinders = cylinders
        self.motor_type = motor_type
        self._temperature = 0

    def inject_gasoline(self, quantity: int) -> None:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
