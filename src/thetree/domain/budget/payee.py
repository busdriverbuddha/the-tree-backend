# src/tree_backend/domain/budget/payee.py

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .category import Category


@dataclass(slots=True)
class Payee:
    name: str
    id: UUID = field(default_factory=uuid4, init=False, repr=False)
    default_category: Category | None = None

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Field 'name' cannot be empty!")
