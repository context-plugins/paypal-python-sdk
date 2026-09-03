from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .card_attributes import CardAttributes, CardAttributesDict
from .card_experience_context import CardExperienceContext, CardExperienceContextDict
from .card_stored_credential import CardStoredCredential, CardStoredCredentialDict
from .network_token import NetworkToken, NetworkTokenDict


class CardRequest(SdkBaseModel):
    """The payment card to use to fund a payment. Can be a credit or debit card. Note: Passing card number, cvv and
    expiry directly via the API requires PCI SAQ D compliance. *PayPal offers a mechanism by which you do not have to
    take on the PCI SAQ D burden by using hosted fields - refer to this Integration Guide*."""

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

    billing_address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    attributes: Optional[CardAttributes] = UNSET
    """Additional attributes associated with the use of this card."""

    vault_id: Optional[str] = UNSET
    """The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the
    saved payment source can be used for future transactions."""

    single_use_token: Optional[str] = UNSET
    """The PayPal-generated, short-lived, one-time-use token, used to communicate payment information to PayPal for
    transaction processing."""

    stored_credential: Optional[CardStoredCredential] = UNSET
    """Provides additional details to process a payment using a ``card`` that has been stored or is intended to be
    stored (also referred to as stored_credential or card-on-file). Parameter compatibility: ``payment_type=ONE_TIME``
    is compatible only with ``payment_initiator=CUSTOMER``. ``usage=FIRST`` is compatible only with
    ``payment_initiator=CUSTOMER``. ``previous_transaction_reference`` or ``previous_network_transaction_reference`` is
    compatible only with ``payment_initiator=MERCHANT``. Only one of the parameters - ``previous_transaction_reference``
    and ``previous_network_transaction_reference`` - can be present in the request."""

    network_token: Optional[NetworkToken] = UNSET
    """The Third Party Network token used to fund a payment."""

    experience_context: Optional[CardExperienceContext] = UNSET
    """Customizes the payer experience during the 3DS Approval for payment."""


class CardRequestDict(TypedDict):
    name: NotRequired[str]
    number: NotRequired[str]
    expiry: NotRequired[str]
    security_code: NotRequired[str]
    billing_address: NotRequired[Address | AddressDict]
    attributes: NotRequired[CardAttributes | CardAttributesDict]
    vault_id: NotRequired[str]
    single_use_token: NotRequired[str]
    stored_credential: NotRequired[CardStoredCredential | CardStoredCredentialDict]
    network_token: NotRequired[NetworkToken | NetworkTokenDict]
    experience_context: NotRequired[CardExperienceContext | CardExperienceContextDict]
