from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .net_amount_breakdown_item import NetAmountBreakdownItem, NetAmountBreakdownItemDict
from .platform_fee import PlatformFee, PlatformFeeDict


class SellerPayableBreakdown(SdkBaseModel):
    """The breakdown of the refund."""

    gross_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    paypal_fee: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    paypal_fee_in_receivable_currency: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    net_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    net_amount_in_receivable_currency: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    platform_fees: Optional[list[PlatformFee]] = UNSET
    """An array of platform or partner fees, commissions, or brokerage fees for the refund."""

    net_amount_breakdown: Optional[list[NetAmountBreakdownItem]] = UNSET
    """An array of breakdown values for the net amount. Returned when the currency of the refund is different from the
    currency of the PayPal account where the payee holds their funds."""

    total_refunded_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class SellerPayableBreakdownDict(TypedDict):
    gross_amount: NotRequired[Money | MoneyDict]
    paypal_fee: NotRequired[Money | MoneyDict]
    paypal_fee_in_receivable_currency: NotRequired[Money | MoneyDict]
    net_amount: NotRequired[Money | MoneyDict]
    net_amount_in_receivable_currency: NotRequired[Money | MoneyDict]
    platform_fees: NotRequired[list[PlatformFee | PlatformFeeDict]]
    net_amount_breakdown: NotRequired[list[NetAmountBreakdownItem | NetAmountBreakdownItemDict]]
    total_refunded_amount: NotRequired[Money | MoneyDict]
