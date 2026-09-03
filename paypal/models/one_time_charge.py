from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class OneTimeCharge(SdkBaseModel):
    """The one-time charge info at the time of checkout."""

    setup_fee: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    taxes: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    product_price: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    subtotal: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    total_amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class OneTimeChargeDict(TypedDict):
    setup_fee: NotRequired[Money | MoneyDict]
    shipping_amount: NotRequired[Money | MoneyDict]
    taxes: NotRequired[Money | MoneyDict]
    product_price: NotRequired[Money | MoneyDict]
    subtotal: NotRequired[Money | MoneyDict]
    total_amount: Money | MoneyDict
