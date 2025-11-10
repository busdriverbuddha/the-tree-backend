# src/tree_backend/domain/budget/budget.py

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from thetree.domain.users import User


@dataclass(slots=True)
class Budget:
    owner: User
    name: str
    created_at: datetime
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self.name = self.name.strip()
        if self.name == "":
            raise ValueError("Field 'name' cannot be empty!")
