def convert_pesos_to_dollars(pesos_type: str, dollar_value: float) -> None:
    pesos = input("How many {} pesos do you have? ".format(pesos_type))
    dollars = round(float(pesos) / dollar_value, 2)
    print("You have ${} dollars".format(str(dollars)))


def main() -> None:
    menu = """
    Welcome to the currency converter

    1 -> Colombian pesos
    2 -> Argentinian pesos
    3 -> Mexican pesos

    Choose an option:
    """
    option = int(input(menu))

    if option == 1:
        convert_pesos_to_dollars("colombian", 3921.17)
    elif option == 2:
        convert_pesos_to_dollars("argentinian", 65)
    elif option == 3:
        convert_pesos_to_dollars("mexican", 24)
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
