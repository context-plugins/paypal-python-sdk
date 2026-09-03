from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .google_pay_card_response import GooglePayCardResponse, GooglePayCardResponseDict
from .phone_number_with_country_code import PhoneNumberWithCountryCode, PhoneNumberWithCountryCodeDict


class GooglePayWalletResponse(SdkBaseModel):
    """Google Pay Wallet payment data."""

    name: Optional[str] = UNSET
    """The full name representation like Mr J Smith."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    phone_number: Optional[PhoneNumberWithCountryCode] = UNSET
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    card: Optional[GooglePayCardResponse] = UNSET
    """The payment card to use to fund a Google Pay payment response. Can be a credit or debit card."""


class GooglePayWalletResponseDict(TypedDict):
    name: NotRequired[str]
    email_address: NotRequired[str]
    phone_number: NotRequired[PhoneNumberWithCountryCode | PhoneNumberWithCountryCodeDict]
    card: NotRequired[GooglePayCardResponse | GooglePayCardResponseDict]
