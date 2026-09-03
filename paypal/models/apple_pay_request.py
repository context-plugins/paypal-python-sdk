from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_attributes import ApplePayAttributes, ApplePayAttributesDict
from .apple_pay_decrypted_token_data import ApplePayDecryptedTokenData, ApplePayDecryptedTokenDataDict
from .apple_pay_experience_context import ApplePayExperienceContext, ApplePayExperienceContextDict
from .card_stored_credential import CardStoredCredential, CardStoredCredentialDict
from .phone_number import PhoneNumber, PhoneNumberDict


class ApplePayRequest(SdkBaseModel):
    """Information needed to pay using ApplePay."""

    id: Optional[str] = UNSET
    """ApplePay transaction identifier, this will be the unique identifier for this transaction provided by Apple. The
    pattern is defined by an external party and supports Unicode."""

    name: Optional[str] = UNSET
    """The full name representation like Mr J Smith."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    phone_number: Optional[PhoneNumber] = UNSET
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    decrypted_token: Optional[ApplePayDecryptedTokenData] = UNSET
    """Information about the Payment data obtained by decrypting Apple Pay token."""

    stored_credential: Optional[CardStoredCredential] = UNSET
    """Provides additional details to process a payment using a ``card`` that has been stored or is intended to be
    stored (also referred to as stored_credential or card-on-file). Parameter compatibility: ``payment_type=ONE_TIME``
    is compatible only with ``payment_initiator=CUSTOMER``. ``usage=FIRST`` is compatible only with
    ``payment_initiator=CUSTOMER``. ``previous_transaction_reference`` or ``previous_network_transaction_reference`` is
    compatible only with ``payment_initiator=MERCHANT``. Only one of the parameters - ``previous_transaction_reference``
    and ``previous_network_transaction_reference`` - can be present in the request."""

    vault_id: Optional[str] = UNSET
    """The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the
    saved payment source can be used for future transactions."""

    attributes: Optional[ApplePayAttributes] = UNSET
    """Additional attributes associated with apple pay."""

    experience_context: Optional[ApplePayExperienceContext] = UNSET
    """Customizes the payer experience during the approval process for the payment."""


class ApplePayRequestDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    email_address: NotRequired[str]
    phone_number: NotRequired[PhoneNumber | PhoneNumberDict]
    decrypted_token: NotRequired[ApplePayDecryptedTokenData | ApplePayDecryptedTokenDataDict]
    stored_credential: NotRequired[CardStoredCredential | CardStoredCredentialDict]
    vault_id: NotRequired[str]
    attributes: NotRequired[ApplePayAttributes | ApplePayAttributesDict]
    experience_context: NotRequired[ApplePayExperienceContext | ApplePayExperienceContextDict]
