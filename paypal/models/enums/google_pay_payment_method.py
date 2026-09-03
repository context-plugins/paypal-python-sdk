from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GooglePayPaymentMethod(str, Enum):
    """The type of the payment credential. Currently, only CARD is supported."""

    CARD = "CARD"
    """CARD is the only value that Google Pay accepts."""

    __str__ = str.__str__


GooglePayPaymentMethodOrStr: TypeAlias = Annotated[
    GooglePayPaymentMethod | str, open_enum_validator(GooglePayPaymentMethod)
]
