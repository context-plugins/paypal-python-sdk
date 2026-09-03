from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .exchange_rate import ExchangeRate, ExchangeRateDict
from .money import Money, MoneyDict


class NetAmountBreakdownItem(SdkBaseModel):
    """The net amount. Returned when the currency of the refund is different from the currency of the PayPal account
    where the merchant holds their funds."""

    payable_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    converted_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    exchange_rate: Optional[ExchangeRate] = UNSET
    """The exchange rate that determines the amount to convert from one currency to another currency."""


class NetAmountBreakdownItemDict(TypedDict):
    payable_amount: NotRequired[Money | MoneyDict]
    converted_amount: NotRequired[Money | MoneyDict]
    exchange_rate: NotRequired[ExchangeRate | ExchangeRateDict]
