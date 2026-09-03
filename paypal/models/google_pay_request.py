from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .assurance_details import AssuranceDetails, AssuranceDetailsDict
from .google_pay_decrypted_token_data import GooglePayDecryptedTokenData, GooglePayDecryptedTokenDataDict
from .google_pay_experience_context import GooglePayExperienceContext, GooglePayExperienceContextDict
from .google_pay_request_card import GooglePayRequestCard, GooglePayRequestCardDict
from .phone_number_with_country_code import PhoneNumberWithCountryCode, PhoneNumberWithCountryCodeDict


class GooglePayRequest(SdkBaseModel):
    """Information needed to pay using Google Pay."""

    name: Optional[str] = UNSET
    """The full name representation like Mr J Smith."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    phone_number: Optional[PhoneNumberWithCountryCode] = UNSET
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    card: Optional[GooglePayRequestCard] = UNSET
    """The payment card used to fund a Google Pay payment. Can be a credit or debit card."""

    decrypted_token: Optional[GooglePayDecryptedTokenData] = UNSET
    """Details shared by Google for the merchant to be shared with PayPal. This is required to process the transaction
    using the Google Pay payment method."""

    assurance_details: Optional[AssuranceDetails] = UNSET
    """Information about cardholder possession validation and cardholder identification and verifications (ID&V)."""

    experience_context: Optional[GooglePayExperienceContext] = UNSET
    """Customizes the payer experience during the approval process for the payment."""


class GooglePayRequestDict(TypedDict):
    name: NotRequired[str]
    email_address: NotRequired[str]
    phone_number: NotRequired[PhoneNumberWithCountryCode | PhoneNumberWithCountryCodeDict]
    card: NotRequired[GooglePayRequestCard | GooglePayRequestCardDict]
    decrypted_token: NotRequired[GooglePayDecryptedTokenData | GooglePayDecryptedTokenDataDict]
    assurance_details: NotRequired[AssuranceDetails | AssuranceDetailsDict]
    experience_context: NotRequired[GooglePayExperienceContext | GooglePayExperienceContextDict]
