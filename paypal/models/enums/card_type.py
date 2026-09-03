from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardType(str, Enum):
    """Type of card. i.e Credit, Debit and so on."""

    CREDIT = "CREDIT"
    """A credit card."""

    DEBIT = "DEBIT"
    """A debit card."""

    PREPAID = "PREPAID"
    """A Prepaid card."""

    STORE = "STORE"
    """A store card."""

    UNKNOWN = "UNKNOWN"
    """Card type cannot be determined."""

    __str__ = str.__str__


CardTypeOrStr: TypeAlias = Annotated[CardType | str, open_enum_validator(CardType)]
