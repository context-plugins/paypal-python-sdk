from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_option import CheckoutOption, CheckoutOptionDict
from .money import Money, MoneyDict
from .tax_amount import TaxAmount, TaxAmountDict


class ItemDetails(SdkBaseModel):
    """The item details."""

    item_code: Optional[str] = UNSET
    """An item code that identifies a merchant's goods or service."""

    item_name: Optional[str] = UNSET
    """The item name."""

    item_description: Optional[str] = UNSET
    """The item description."""

    item_options: Optional[str] = UNSET
    """The item options. Describes option choices on the purchase of the item in some detail."""

    item_quantity: Optional[str] = UNSET
    """The number of purchased units of goods or a service."""

    item_unit_price: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    item_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    discount_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    adjustment_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    gift_wrap_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    tax_percentage: Optional[str] = UNSET
    """The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as
    ``19.99``."""

    tax_amounts: Optional[list[TaxAmount]] = UNSET
    """An array of tax amounts levied by a government on the purchase of goods or services."""

    basic_shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    extra_shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    handling_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    insurance_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    total_item_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    invoice_number: Optional[str] = UNSET
    """The invoice number. An alphanumeric string that identifies a billing for a merchant."""

    checkout_options: Optional[list[CheckoutOption]] = UNSET
    """An array of checkout options. Each option has a name and value."""


class ItemDetailsDict(TypedDict):
    item_code: NotRequired[str]
    item_name: NotRequired[str]
    item_description: NotRequired[str]
    item_options: NotRequired[str]
    item_quantity: NotRequired[str]
    item_unit_price: NotRequired[Money | MoneyDict]
    item_amount: NotRequired[Money | MoneyDict]
    discount_amount: NotRequired[Money | MoneyDict]
    adjustment_amount: NotRequired[Money | MoneyDict]
    gift_wrap_amount: NotRequired[Money | MoneyDict]
    tax_percentage: NotRequired[str]
    tax_amounts: NotRequired[list[TaxAmount | TaxAmountDict]]
    basic_shipping_amount: NotRequired[Money | MoneyDict]
    extra_shipping_amount: NotRequired[Money | MoneyDict]
    handling_amount: NotRequired[Money | MoneyDict]
    insurance_amount: NotRequired[Money | MoneyDict]
    total_item_amount: NotRequired[Money | MoneyDict]
    invoice_number: NotRequired[str]
    checkout_options: NotRequired[list[CheckoutOption | CheckoutOptionDict]]
