import os
import csv
from typing import List, Dict

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

    def update_client(self, updated_client: Client) -> None:
        clients = self.list_clients()

        updated_clients = list(
            map(
                lambda c: updated_client.to_dict()
                if c.get('uid') == updated_client.uid
                else c,
                clients,
            )
        )

        self._save_to_disk(updated_clients)

    def _save_to_disk(self, clients: List[Dict[str, any]]) -> None:
        tmp_table_name = self.table_name + '.tmp'

        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
