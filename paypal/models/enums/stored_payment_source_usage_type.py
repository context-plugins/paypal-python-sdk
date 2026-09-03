from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoredPaymentSourceUsageType(str, Enum):
    """Indicates if this is a ``first`` or ``subsequent`` payment using a stored payment source (also referred to as
    stored credential or card on file)."""

    FIRST = "FIRST"
    """Indicates the Initial/First payment with a payment_source that is intended to be stored upon successful
    processing of the payment."""

    SUBSEQUENT = "SUBSEQUENT"
    """Indicates a payment using a stored payment_source which has been successfully used previously for a payment."""

    DERIVED = "DERIVED"
    """Indicates that PayPal will derive the value of ``FIRST`` or ``SUBSEQUENT`` based on data available to PayPal."""

    __str__ = str.__str__


StoredPaymentSourceUsageTypeOrStr: TypeAlias = Annotated[
    StoredPaymentSourceUsageType | str, open_enum_validator(StoredPaymentSourceUsageType)
]
