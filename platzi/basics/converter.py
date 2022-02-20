PESOS_VALUE = 0.00025
DOLLAR_VALUE = 3921.17


def convert_pesos_to_dollars(pesos: float) -> float:
    return round(pesos / DOLLAR_VALUE, 2)


def convert_dollars_to_pesos(dollars: float) -> float:
    return round(dollars / PESOS_VALUE, 2)


def main() -> None:
    option = int(
        input(
            "Select the option: \n [1] Convert colombian pesos to dollars \n [2] Convert dollars to colombian pesos: "
        )
    )

    if option == 1:
        pesos = input("How many colombian pesos do you have? ")
        dollars = convert_pesos_to_dollars(float(pesos))
        print("You have ${} dollars".format(str(dollars)))
    elif option == 2:
        dollars = input("How many dollars do you have? ")
        pesos = convert_dollars_to_pesos(float(dollars))
        print("You have ${} colombian pesos".format(str(pesos)))
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
