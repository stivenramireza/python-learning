import uuid
from typing import List, Dict


class Client:
    def __init__(
        self,
        name: str,
        company: str,
        email: str,
        position: str,
        uid: int = None,
    ) -> None:
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self) -> Dict[str, any]:
        return vars(self)

    @staticmethod
    def schema() -> List[str]:
        return ['name', 'company', 'email', 'position', 'uid']
