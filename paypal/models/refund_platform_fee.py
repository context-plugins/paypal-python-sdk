from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .money import Money, MoneyDict


class RefundPlatformFee(SdkBaseModel):
    """The platform or partner fee, commission, or brokerage fee that is associated with the transaction. Not a separate
    or isolated transaction leg from the external perspective. The platform fee is limited in scope and is always
    associated with the original payment for the purchase unit."""

    amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class RefundPlatformFeeDict(TypedDict):
    amount: Money | MoneyDict
