from venv import create


clients = "Pablo,Ricardo,"


def create_client(client_name: str) -> None:
    global clients
    clients += client_name
    _add_comma()


def get_clients() -> None:
    global clients
    print(clients)


def _add_comma() -> None:
    global clients
    clients += ","


def main() -> None:
    get_clients()
    create_client("David")
    get_clients()


if __name__ == "__main__":
    main()
