from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .line_item import LineItem, LineItemDict
from .money import Money, MoneyDict


class Level3CardProcessingData(SdkBaseModel):
    """The level 3 card processing data collections, If your merchant account has been configured for Level 3 processing
    this field will be passed to the processor on your behalf. Please contact your PayPal Technical Account Manager to
    define level 3 data for your business."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    duty_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    discount_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    ships_from_postal_code: Optional[str] = UNSET
    """Use this field to specify the postal code of the shipping location."""

    line_items: Optional[list[LineItem]] = UNSET
    """A list of the items that were purchased with this payment. If your merchant account has been configured for Level
    3 processing this field will be passed to the processor on your behalf."""


class Level3CardProcessingDataDict(TypedDict):
    shipping_amount: NotRequired[Money | MoneyDict]
    duty_amount: NotRequired[Money | MoneyDict]
    discount_amount: NotRequired[Money | MoneyDict]
    shipping_address: NotRequired[Address | AddressDict]
    ships_from_postal_code: NotRequired[str]
    line_items: NotRequired[list[LineItem | LineItemDict]]
