# src/tree_backend/domain/budget/currency.py

from dataclasses import dataclass, field


@dataclass(slots=True, order=True, eq=True)
class Currency:
    code: str = field(compare=True)
    name: str

    def __post_init__(self):
        self.name = self.name.strip()
        if self.name == "":
            raise ValueError("Field 'name' cannot be empty!")

        self.code = self.code.strip()
        if self.name == "":
            raise ValueError("Field 'code' cannot be empty!")
