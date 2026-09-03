from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.card_type import CardTypeOrStr
from .enums.subscriptions_card_brand import SubscriptionsCardBrandOrStr
from .subscriptions_card_attributes import SubscriptionsCardAttributes, SubscriptionsCardAttributesDict


class SubscriptionCardRequest(SdkBaseModel):
    """The payment card to use to fund a payment. Can be a credit or debit card."""

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

    type_: Optional[CardTypeOrStr] = Field(default=UNSET, alias="type")
    """Type of card. i.e Credit, Debit and so on."""

    brand: Optional[SubscriptionsCardBrandOrStr] = UNSET
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    billing_address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    attributes: Optional[SubscriptionsCardAttributes] = UNSET
    """Additional attributes associated with the use of this card."""


class SubscriptionCardRequestDict(TypedDict):
    name: NotRequired[str]
    number: NotRequired[str]
    expiry: NotRequired[str]
    security_code: NotRequired[str]
    type_: NotRequired[CardTypeOrStr]
    brand: NotRequired[SubscriptionsCardBrandOrStr]
    billing_address: NotRequired[Address | AddressDict]
    attributes: NotRequired[SubscriptionsCardAttributes | SubscriptionsCardAttributesDict]
