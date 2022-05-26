import csv

from clients.models import Client


class ClientService:
    def __init__(self, table_name: str) -> None:
        self.table_name = table_name

    def create_client(self, client: Client) -> None:
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self) -> None:
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)
