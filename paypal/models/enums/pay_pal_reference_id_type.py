from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayPalReferenceIdType(str, Enum):
    """The PayPal reference ID type."""

    ODR = "ODR"
    """An order ID."""

    TXN = "TXN"
    """A transaction ID."""

    SUB = "SUB"
    """A subscription ID."""

    PAP = "PAP"
    """A pre-approved payment ID."""

    __str__ = str.__str__


PayPalReferenceIdTypeOrStr: TypeAlias = Annotated[
    PayPalReferenceIdType | str, open_enum_validator(PayPalReferenceIdType)
]
