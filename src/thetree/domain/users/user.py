# src/tree_backend/domain/users/user.py

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class User:
    name: str
    id: UUID = field(default_factory=uuid4, init=False)

    def __post_init__(self):
        self.name = self.name.strip()
        if self.name == "":
            raise ValueError("Field 'name' cannot be empty!")
