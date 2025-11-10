# src/tree_backend/domain/budget/supercategory.py

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .budget import Budget


@dataclass(slots=True)
class Supercategory:
    budget: Budget
    name: str
    id: UUID = field(default_factory=uuid4, init=False, repr=False)

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Field 'name' cannot be empty!")
