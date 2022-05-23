import sys
from typing import Dict

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]

CLIENT_NO_EXISTS = 'Client is not in the client\'s list'


def create_client(client: Dict[str, any]) -> None:
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s name')


def list_clients() -> None:
    for idx, client in enumerate(clients):
        print(
            '{uid} | {name} | {company} | {email} | {position}'.format(
                uid=idx,
                name=client.get('name'),
                company=client.get('company'),
                email=client.get('email'),
                position=client.get('position'),
            )
        )


def update_client(client_name: str, updated_client_name: str) -> None:
    global clients

    exists_client = False
    for client in clients:
        if client_name in client.values():
            exists_client = True
            client.update({'name': updated_client_name})

    if not exists_client:
        print(CLIENT_NO_EXISTS)


def delete_client(client_name: str) -> None:
    global clients

    exists_client = False
    for client in clients:
        if client_name in client.values():
            exists_client = True
            clients.remove(client)

    if not exists_client:
        print(CLIENT_NO_EXISTS)


def search_client(client_name: str) -> bool:
    for client in clients:
        if client.get('name') != client_name:
            continue
        else:
            return True


def _print_welcome() -> None:
    print(
        '''
    WELCOME TO STIVENRAMIREZA SALES

    What would you like to do today?

    - [C]reate client
    - [L]ist clients
    - [U]pdate client
    - [D]elete client
    - [S]earch client
    '''
    )


def _get_client_field(field_name: str) -> None:
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field


def _get_client_name() -> str:
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def main() -> None:
    _print_welcome()

    command = input()
    command = command.upper()

    match command:
        case 'C':
            client = {
                'name': _get_client_field('name'),
                'company': _get_client_field('company'),
                'email': _get_client_field('email'),
                'position': _get_client_field('position'),
            }
            create_client(client)
            list_clients()
        case 'L':
            list_clients()
        case 'D':
            client_name = _get_client_name()
            delete_client(client_name)
            list_clients()
        case 'U':
            client_name = _get_client_name()
            updated_client_name = input('What is the updated client name? ')
            update_client(client_name, updated_client_name)
            list_clients()
        case 'S':
            client_name = _get_client_name()
            is_client_found = search_client(client_name)

            if is_client_found:
                print('The client is in the client\'s list')
            else:
                print(
                    'The client {} is not in the client\'s list'.format(
                        client_name
                    )
                )
        case _:
            print('Invalid command')


if __name__ == '__main__':
    main()
