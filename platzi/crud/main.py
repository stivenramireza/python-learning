clients = "Pablo,Ricardo,"

CLIENT_NO_EXISTS = "Client is not in the client's list"


def create_client(client_name: str) -> None:
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("Client already is in the client's name")


def list_clients() -> None:
    global clients
    print(clients)


def update_client(client_name: str, updated_client_name: str) -> None:
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", updated_client_name)
    else:
        print(CLIENT_NO_EXISTS)


def delete_client(client_name: str) -> None:
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", "")
    else:
        print(CLIENT_NO_EXISTS)


def _add_comma() -> None:
    global clients
    clients += ","


def _print_welcome() -> None:
    print("WELCOME TO STIVENRAMIREZA SALES")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")


def _get_client_name() -> str:
    return input("What is the client name? ")


def main() -> None:
    _print_welcome()

    command = input()
    command = command.upper()

    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "U":
        client_name = _get_client_name()
        updated_client_name = input("What is the updated client name? ")
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
