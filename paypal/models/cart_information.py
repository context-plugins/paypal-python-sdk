from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_details import ItemDetails, ItemDetailsDict


class CartInformation(SdkBaseModel):
    """The cart information."""

    item_details: Optional[list[ItemDetails]] = UNSET
    """An array of item details."""

    tax_inclusive: Optional[bool] = UNSET
    """Indicates whether the item amount or the shipping amount already includes tax."""

    paypal_invoice_id: Optional[str] = UNSET
    """The ID of the invoice. Appears for only PayPal-generated invoices."""


class CartInformationDict(TypedDict):
    item_details: NotRequired[list[ItemDetails | ItemDetailsDict]]
    tax_inclusive: NotRequired[bool]
    paypal_invoice_id: NotRequired[str]
