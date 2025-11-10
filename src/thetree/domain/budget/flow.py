# src/tree_backend/domain/budget/flow.py

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from functools import total_ordering
from uuid import UUID, uuid4

from .account import Account
from .money import Money
from .payee import Payee


class FlowType(Enum):
    INFLOW = "inflow"
    OUTFLOW = "outflow"


@total_ordering
@dataclass(slots=True, eq=True)
class Flow:
    created_at: datetime
    bank_date: datetime
    flow_type: FlowType
    money: Money
    account: Account
    payee: Payee | None = None
    transfer: "Flow | None" = None
    id: UUID = field(default_factory=uuid4, init=False, repr=False)
    comments: str = ""

    def __eq__(self, other):
        if not isinstance(other, Flow):
            return NotImplemented
        return self.id == other.id

    def __lt__(self, other):
        if not isinstance(other, Flow):
            return NotImplemented
        return self.created_at < other.created_at
