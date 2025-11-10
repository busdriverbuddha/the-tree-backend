# src/tree_backend/domain/budget/account.py

from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID, uuid4

from .budget import Budget
from .currency import Currency


class AccountType(Enum):
    CHECKING = "checking"
    CREDIT_CARD = "credit_card"
    SAVINGS = "savings"
    CASH = "cash"


@dataclass(slots=True)
class Account:
    account_type: AccountType
    budget: Budget
    created_at: datetime
    currency: Currency
    name: str
    id: UUID = field(default_factory=uuid4, init=False, repr=False)
    closed_at: datetime | None = None

    def __post_init__(self):
        self.name = self.name.strip()
        if self.name == "":
            raise ValueError("Field 'name' cannot be empty!")

        if self.closed_at is not None and self.closed_at < self.created_at:
            raise ValueError("Cannot have 'closed_at' before 'created_at'!")

    @property
    def is_active(self) -> bool:
        return self.closed_at is None
