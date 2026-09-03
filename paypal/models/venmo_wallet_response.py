from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.return_flow import ReturnFlowOrStr
from .name import Name, NameDict
from .phone_number import PhoneNumber, PhoneNumberDict
from .venmo_wallet_attributes_response import VenmoWalletAttributesResponse, VenmoWalletAttributesResponseDict


class VenmoWalletResponse(SdkBaseModel):
    """Venmo wallet response."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    account_id: Optional[str] = UNSET
    """The PayPal payer ID, which is a masked version of the PayPal account number intended for use with third parties.
    The account number is reversibly encrypted and a proprietary variant of Base32 is used to encode the result."""

    user_name: Optional[str] = UNSET
    """The Venmo user name chosen by the user, also know as a Venmo handle."""

    name: Optional[Name] = UNSET
    """The name of the party."""

    phone_number: Optional[PhoneNumber] = UNSET
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    return_flow: Optional[ReturnFlowOrStr] = UNSET
    """Merchant preference on how the buyer can navigate back to merchant website post approving the transaction on the
    Venmo App."""

    attributes: Optional[VenmoWalletAttributesResponse] = UNSET
    """Additional attributes associated with the use of a Venmo Wallet."""


class VenmoWalletResponseDict(TypedDict):
    email_address: NotRequired[str]
    account_id: NotRequired[str]
    user_name: NotRequired[str]
    name: NotRequired[Name | NameDict]
    phone_number: NotRequired[PhoneNumber | PhoneNumberDict]
    address: NotRequired[Address | AddressDict]
    return_flow: NotRequired[ReturnFlowOrStr]
    attributes: NotRequired[VenmoWalletAttributesResponse | VenmoWalletAttributesResponseDict]
