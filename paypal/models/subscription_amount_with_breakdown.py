from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class SubscriptionAmountWithBreakdown(SdkBaseModel):
    """The breakdown details for the amount. Includes the gross, tax, fee, and shipping amounts."""

    gross_amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    total_item_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    fee_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    tax_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    net_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class SubscriptionAmountWithBreakdownDict(TypedDict):
    gross_amount: MoneyDict
    total_item_amount: NotRequired[MoneyDict]
    fee_amount: NotRequired[MoneyDict]
    shipping_amount: NotRequired[MoneyDict]
    tax_amount: NotRequired[MoneyDict]
    net_amount: NotRequired[MoneyDict]
