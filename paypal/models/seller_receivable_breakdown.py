from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .exchange_rate import ExchangeRate, ExchangeRateDict
from .money import Money, MoneyDict
from .platform_fee import PlatformFee, PlatformFeeDict


class SellerReceivableBreakdown(SdkBaseModel):
    """The detailed breakdown of the capture activity. This is not available for transactions that are in pending
    state."""

    gross_amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    paypal_fee: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    paypal_fee_in_receivable_currency: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    net_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    receivable_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    exchange_rate: Optional[ExchangeRate] = UNSET
    """The exchange rate that determines the amount to convert from one currency to another currency."""

    platform_fees: Optional[list[PlatformFee]] = UNSET
    """An array of platform or partner fees, commissions, or brokerage fees that associated with the captured
    payment."""


class SellerReceivableBreakdownDict(TypedDict):
    gross_amount: Money | MoneyDict
    paypal_fee: NotRequired[Money | MoneyDict]
    paypal_fee_in_receivable_currency: NotRequired[Money | MoneyDict]
    net_amount: NotRequired[Money | MoneyDict]
    receivable_amount: NotRequired[Money | MoneyDict]
    exchange_rate: NotRequired[ExchangeRate | ExchangeRateDict]
    platform_fees: NotRequired[list[PlatformFee | PlatformFeeDict]]
