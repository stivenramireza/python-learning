import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients() -> None:
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option(
    '-c', '--company', type=str, prompt=True, help='The client company'
)
@click.option('-e', '--email', type=str, prompt=True, help='The client email')
@click.option(
    '-p', '--position', type=str, prompt=True, help='The client position'
)
@click.pass_context
def create(
    ctx: object, name: str, company: str, email: str, position: str
) -> None:
    """Creates a new client"""
    client = Client(name, company, email, position)

    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx: object) -> None:
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()

    click.echo('  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION  ')
    click.echo('*' * 100)

    for client in clients:
        click.echo(
            '{uid}  |  {name}  |  {company}  |  {email}  |  {position}'.format(
                uid=client.get('uid'),
                name=client.get('name'),
                company=client.get('company'),
                email=client.get('email'),
                position=client.get('position'),
            )
        )


@clients.command()
@click.pass_context
def update(ctx: object, client_uid: int) -> None:
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx: object, client_uid: int) -> None:
    """Deletes a client"""
    pass


all = clients
