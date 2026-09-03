from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.card_brand import CardBrandOrStr


class PaymentTokenRequestCard(SdkBaseModel):
    """A Resource representing a request to vault a Card."""

    name: Optional[str] = UNSET
    """The card holder's name as it appears on the card."""

    number: Optional[str] = UNSET
    """The primary account number (PAN) for the payment card."""

    expiry: Optional[str] = UNSET
    """The year and month, in ISO-8601 ``YYYY-MM`` date format. See `Internet date and time format
    <https://tools.ietf.org/html/rfc3339#section-5.6>`__."""

    security_code: Optional[str] = UNSET
    """The three- or four-digit security code of the card. Also known as the CVV, CVC, CVN, CVE, or CID. This parameter
    cannot be present in the request when ``payment_initiator=MERCHANT``."""

    brand: Optional[CardBrandOrStr] = UNSET
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    billing_address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""


class PaymentTokenRequestCardDict(TypedDict):
    name: NotRequired[str]
    number: NotRequired[str]
    expiry: NotRequired[str]
    security_code: NotRequired[str]
    brand: NotRequired[CardBrandOrStr]
    billing_address: NotRequired[Address | AddressDict]
