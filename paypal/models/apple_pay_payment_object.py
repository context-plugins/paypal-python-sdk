from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_attributes_response import ApplePayAttributesResponse, ApplePayAttributesResponseDict
from .apple_pay_card_response import ApplePayCardResponse, ApplePayCardResponseDict
from .card_stored_credential import CardStoredCredential, CardStoredCredentialDict
from .phone_number import PhoneNumber, PhoneNumberDict


class ApplePayPaymentObject(SdkBaseModel):
    """Information needed to pay using ApplePay."""

    id: Optional[str] = UNSET
    """ApplePay transaction identifier, this will be the unique identifier for this transaction provided by Apple. The
    pattern is defined by an external party and supports Unicode."""

    token: Optional[str] = UNSET
    """Encrypted ApplePay token, containing card information. This token would be base64encoded. The pattern is defined
    by an external party and supports Unicode."""

    name: Optional[str] = UNSET
    """The full name representation like Mr J Smith."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    phone_number: Optional[PhoneNumber] = UNSET
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    card: Optional[ApplePayCardResponse] = UNSET
    """The Card from Apple Pay Wallet used to fund the payment."""

    attributes: Optional[ApplePayAttributesResponse] = UNSET
    """Additional attributes associated with the use of Apple Pay."""

    stored_credential: Optional[CardStoredCredential] = UNSET
    """Provides additional details to process a payment using a ``card`` that has been stored or is intended to be
    stored (also referred to as stored_credential or card-on-file). Parameter compatibility: ``payment_type=ONE_TIME``
    is compatible only with ``payment_initiator=CUSTOMER``. ``usage=FIRST`` is compatible only with
    ``payment_initiator=CUSTOMER``. ``previous_transaction_reference`` or ``previous_network_transaction_reference`` is
    compatible only with ``payment_initiator=MERCHANT``. Only one of the parameters - ``previous_transaction_reference``
    and ``previous_network_transaction_reference`` - can be present in the request."""


class ApplePayPaymentObjectDict(TypedDict):
    id: NotRequired[str]
    token: NotRequired[str]
    name: NotRequired[str]
    email_address: NotRequired[str]
    phone_number: NotRequired[PhoneNumber | PhoneNumberDict]
    card: NotRequired[ApplePayCardResponse | ApplePayCardResponseDict]
    attributes: NotRequired[ApplePayAttributesResponse | ApplePayAttributesResponseDict]
    stored_credential: NotRequired[CardStoredCredential | CardStoredCredentialDict]
