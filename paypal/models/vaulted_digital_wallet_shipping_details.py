from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.fulfillment_type import FulfillmentTypeOrStr
from .phone_number_with_country_code import PhoneNumberWithCountryCode, PhoneNumberWithCountryCodeDict
from .shipping_name import ShippingName, ShippingNameDict


class VaultedDigitalWalletShippingDetails(SdkBaseModel):
    """The shipping details."""

    name: Optional[ShippingName] = UNSET
    """The name of the party."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    phone_number: Optional[PhoneNumberWithCountryCode] = UNSET
    """The phone number, in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    type_: Optional[FulfillmentTypeOrStr] = Field(default=UNSET, alias="type")
    """A classification for the method of purchase fulfillment (e.g shipping, in-store pickup, etc). Either ``type`` or
    ``options`` may be present, but not both."""

    address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""


class VaultedDigitalWalletShippingDetailsDict(TypedDict):
    name: NotRequired[ShippingName | ShippingNameDict]
    email_address: NotRequired[str]
    phone_number: NotRequired[PhoneNumberWithCountryCode | PhoneNumberWithCountryCodeDict]
    type_: NotRequired[FulfillmentTypeOrStr]
    address: NotRequired[Address | AddressDict]
