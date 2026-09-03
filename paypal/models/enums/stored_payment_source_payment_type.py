from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoredPaymentSourcePaymentType(str, Enum):
    """Indicates the type of the stored payment_source payment."""

    ONE_TIME = "ONE_TIME"
    """One Time payment such as online purchase or donation. (e.g. Checkout with one-click)."""

    RECURRING = "RECURRING"
    """Payment which is part of a series of payments with fixed or variable amounts, following a fixed time interval.
    (e.g. Subscription payments)."""

    UNSCHEDULED = "UNSCHEDULED"
    """Payment which is part of a series of payments that occur on a non-fixed schedule and/or have variable amounts.
    (e.g. Account Topup payments)."""

    __str__ = str.__str__


StoredPaymentSourcePaymentTypeOrStr: TypeAlias = Annotated[
    StoredPaymentSourcePaymentType | str, open_enum_validator(StoredPaymentSourcePaymentType)
]
