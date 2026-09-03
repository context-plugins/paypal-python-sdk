from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class AmountBreakdown(SdkBaseModel):
    """The breakdown of the amount. Breakdown provides details such as total item amount, total tax amount, shipping,
    handling, insurance, and discounts, if any."""

    item_total: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    handling: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    tax_total: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    insurance: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_discount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    discount: Optional[Money] = UNSET
    """The discount amount and currency code. For list of supported currencies and decimal precision, see the PayPal
    REST APIs Currency Codes."""


class AmountBreakdownDict(TypedDict):
    item_total: NotRequired[Money | MoneyDict]
    shipping: NotRequired[Money | MoneyDict]
    handling: NotRequired[Money | MoneyDict]
    tax_total: NotRequired[Money | MoneyDict]
    insurance: NotRequired[Money | MoneyDict]
    shipping_discount: NotRequired[Money | MoneyDict]
    discount: NotRequired[Money | MoneyDict]
