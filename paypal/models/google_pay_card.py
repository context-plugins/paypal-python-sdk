from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.card_brand import CardBrandOrStr
from .enums.card_type import CardTypeOrStr


class GooglePayCard(SdkBaseModel):
    """The payment card used to fund a Google Pay payment. Can be a credit or debit card."""

    name: Optional[str] = UNSET
    """The card holder's name as it appears on the card."""

    number: Optional[str] = UNSET
    """The primary account number (PAN) for the payment card."""

    expiry: Optional[str] = UNSET
    """The year and month, in ISO-8601 ``YYYY-MM`` date format. See `Internet date and time format
    <https://tools.ietf.org/html/rfc3339#section-5.6>`__."""

    last_digits: Optional[str] = UNSET
    """The last digits of the payment card."""

    type_: Optional[CardTypeOrStr] = Field(default=UNSET, alias="type")
    """Type of card. i.e Credit, Debit and so on."""

    brand: Optional[CardBrandOrStr] = UNSET
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    billing_address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""


class GooglePayCardDict(TypedDict):
    name: NotRequired[str]
    number: NotRequired[str]
    expiry: NotRequired[str]
    last_digits: NotRequired[str]
    type_: NotRequired[CardTypeOrStr]
    brand: NotRequired[CardBrandOrStr]
    billing_address: NotRequired[Address | AddressDict]
