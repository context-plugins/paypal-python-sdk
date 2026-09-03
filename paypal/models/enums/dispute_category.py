from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisputeCategory(str, Enum):
    """The condition that is covered for the transaction."""

    ITEM_NOT_RECEIVED = "ITEM_NOT_RECEIVED"
    """The payer paid for an item that they did not receive."""

    UNAUTHORIZED_TRANSACTION = "UNAUTHORIZED_TRANSACTION"
    """The payer did not authorize the payment."""

    __str__ = str.__str__


DisputeCategoryOrStr: TypeAlias = Annotated[DisputeCategory | str, open_enum_validator(DisputeCategory)]
