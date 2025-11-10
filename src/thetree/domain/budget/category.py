# src/tree_backend/domain/budget/category.py

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .supercategory import Supercategory


@dataclass(slots=True)
class Category:
    supercategory: Supercategory
    name: str
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self.name = self.name.strip()
        if self.name == "":
            raise ValueError("Field 'name' cannot be empty!")
