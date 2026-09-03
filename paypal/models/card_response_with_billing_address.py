from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict


class CardResponseWithBillingAddress(SdkBaseModel):
    """The payment card used to fund the payment. Card can be a credit or debit card."""

    name: Optional[str] = UNSET
    """The card holder's name as it appears on the card."""

    billing_address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    expiry: Optional[str] = UNSET
    """The year and month, in ISO-8601 ``YYYY-MM`` date format. See `Internet date and time format
    <https://tools.ietf.org/html/rfc3339#section-5.6>`__."""

    currency_code: Optional[str] = UNSET
    """The `three-character ISO-4217 currency code <https://developer.paypal.com/api/rest/reference/currency-codes/>`__
    that identifies the currency."""


class CardResponseWithBillingAddressDict(TypedDict):
    name: NotRequired[str]
    billing_address: NotRequired[Address | AddressDict]
    expiry: NotRequired[str]
    currency_code: NotRequired[str]
