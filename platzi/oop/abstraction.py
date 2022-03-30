class WashingMachine:
    def __init__(self) -> None:
        pass

    def wash(self, temperature: str = "hot") -> None:
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_water_tank(self, temperature: str) -> None:
        print(f"Filling the water tank {temperature}")

    def _add_soap(self) -> None:
        print("Adding soap")

    def _wash(self) -> None:
        print("Washing the clothes")

    def _centrifuge(self) -> None:
        print("Centrifuging the clothes")


def main() -> None:
    washing_machine = WashingMachine()
    washing_machine.wash()


if __name__ == "__main__":
    main()
