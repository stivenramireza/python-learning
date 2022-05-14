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
        clients = clients.replace(client_name, updated_client_name)
    else:
        print(CLIENT_NO_EXISTS)


def delete_client(client_name: str) -> None:
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, "")
    else:
        print(CLIENT_NO_EXISTS)


def search_client(client_name: str) -> bool:
    clients_list = clients.split(",")

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_comma() -> None:
    global clients
    clients += ","


def _print_welcome() -> None:
    print(
        """
    WELCOME TO STIVENRAMIREZA SALES

    What would you like to do today?

    - [C]reate client
    - [L]ist clients
    - [U]pdate client
    - [D]elete client
    - [S]earch client
    """
    )


def _get_client_name() -> str:
    return input("What is the client name? ")


def main() -> None:
    _print_welcome()

    command = input()
    command = command.upper()

    match command:
        case "C":
            client_name = _get_client_name()
            create_client(client_name)
            list_clients()
        case "L":
            list_clients()
        case "D":
            client_name = _get_client_name()
            delete_client(client_name)
            list_clients()
        case "U":
            client_name = _get_client_name()
            updated_client_name = input("What is the updated client name? ")
            update_client(client_name, updated_client_name)
            list_clients()
        case "S":
            client_name = _get_client_name()
            is_client_found = search_client(client_name)

            if is_client_found:
                print("The client is in the client's list")
            else:
                print(f"The client {client_name} is not in the client's list")
        case _:
            print("Invalid command")


if __name__ == "__main__":
    main()
