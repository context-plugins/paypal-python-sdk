from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TokenType(str, Enum):
    """The tokenization method that generated the ID."""

    BILLING_AGREEMENT = "BILLING_AGREEMENT"
    """The PayPal billing agreement ID. References an approved recurring payment for goods or services."""

    __str__ = str.__str__


TokenTypeOrStr: TypeAlias = Annotated[TokenType | str, open_enum_validator(TokenType)]
