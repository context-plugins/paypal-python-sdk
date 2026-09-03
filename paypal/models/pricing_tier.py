from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class PricingTier(SdkBaseModel):
    """The pricing tier details."""

    starting_quantity: str
    """The starting quantity for the tier."""

    ending_quantity: Optional[str] = UNSET
    """The ending quantity for the tier. Optional for the last tier."""

    amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class PricingTierDict(TypedDict):
    starting_quantity: str
    ending_quantity: NotRequired[str]
    amount: Money | MoneyDict
