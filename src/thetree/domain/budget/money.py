from dataclasses import dataclass, field

from .currency import Currency


@dataclass(frozen=True, slots=True, eq=True)
class Money:
    amount_cents: int = field(compare=True)
    currency: Currency = field(compare=True)

    def __post_init__(self):
        if self.amount_cents < 0:
            raise ValueError("Field 'amount_cents' must be positive!")
