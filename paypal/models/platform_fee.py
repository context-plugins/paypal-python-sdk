from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .payee_base import PayeeBase, PayeeBaseDict


class PlatformFee(SdkBaseModel):
    """The platform or partner fee, commission, or brokerage fee that is associated with the transaction. Not a separate
    or isolated transaction leg from the external perspective. The platform fee is limited in scope and is always
    associated with the original payment for the purchase unit."""

    amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    payee: Optional[PayeeBase] = UNSET
    """The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the
    payee."""


class PlatformFeeDict(TypedDict):
    amount: Money | MoneyDict
    payee: NotRequired[PayeeBase | PayeeBaseDict]
