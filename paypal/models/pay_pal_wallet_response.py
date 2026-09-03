from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.experience_status import ExperienceStatusOrStr
from .enums.pay_pal_wallet_account_verification_status import PayPalWalletAccountVerificationStatusOrStr
from .enums.phone_type import PhoneTypeOrStr
from .name import Name, NameDict
from .pay_pal_wallet_attributes_response import PayPalWalletAttributesResponse, PayPalWalletAttributesResponseDict
from .pay_pal_wallet_stored_credential import PayPalWalletStoredCredential, PayPalWalletStoredCredentialDict
from .phone_number import PhoneNumber, PhoneNumberDict
from .tax_info import TaxInfo, TaxInfoDict


class PayPalWalletResponse(SdkBaseModel):
    """The PayPal Wallet response."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    account_id: Optional[str] = UNSET
    """The PayPal payer ID, which is a masked version of the PayPal account number intended for use with third parties.
    The account number is reversibly encrypted and a proprietary variant of Base32 is used to encode the result."""

    account_status: Optional[PayPalWalletAccountVerificationStatusOrStr] = UNSET
    """The account status indicates whether the buyer has verified the financial details associated with their PayPal
    account."""

    name: Optional[Name] = UNSET
    """The name of the party."""

    phone_type: Optional[PhoneTypeOrStr] = UNSET
    """The phone type."""

    phone_number: Optional[PhoneNumber] = UNSET
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    birth_date: Optional[str] = UNSET
    """The stand-alone date, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. To
    represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone
    data. Whenever possible, use the standard ``date_time`` type. This regular expression does not validate all dates.
    For example, February 31 is valid and nothing is known about leap years."""

    business_name: Optional[str] = UNSET
    """The business name of the PayPal account holder (populated for business accounts only)"""

    tax_info: Optional[TaxInfo] = UNSET
    """The tax ID of the customer. The customer is also known as the payer. Both ``tax_id`` and ``tax_id_type`` are
    required."""

    address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    attributes: Optional[PayPalWalletAttributesResponse] = UNSET
    """Additional attributes associated with the use of a PayPal Wallet."""

    stored_credential: Optional[PayPalWalletStoredCredential] = UNSET
    """Provides additional details to process a payment using the PayPal wallet billing agreement or a vaulted payment
    method that has been stored or is intended to be stored."""

    experience_status: Optional[ExperienceStatusOrStr] = UNSET
    """This field indicates the status of PayPal's Checkout experience throughout the order lifecycle. The values
    reflect the current stage of the checkout process."""


class PayPalWalletResponseDict(TypedDict):
    email_address: NotRequired[str]
    account_id: NotRequired[str]
    account_status: NotRequired[PayPalWalletAccountVerificationStatusOrStr]
    name: NotRequired[Name | NameDict]
    phone_type: NotRequired[PhoneTypeOrStr]
    phone_number: NotRequired[PhoneNumber | PhoneNumberDict]
    birth_date: NotRequired[str]
    business_name: NotRequired[str]
    tax_info: NotRequired[TaxInfo | TaxInfoDict]
    address: NotRequired[Address | AddressDict]
    attributes: NotRequired[PayPalWalletAttributesResponse | PayPalWalletAttributesResponseDict]
    stored_credential: NotRequired[PayPalWalletStoredCredential | PayPalWalletStoredCredentialDict]
    experience_status: NotRequired[ExperienceStatusOrStr]
