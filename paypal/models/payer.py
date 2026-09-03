from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .name import Name, NameDict
from .phone_with_type import PhoneWithType, PhoneWithTypeDict
from .tax_info import TaxInfo, TaxInfoDict


class Payer(SdkBaseModel):
    """The customer who approves and pays for the order. The customer is also known as the payer."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    payer_id: Optional[str] = UNSET
    """The account identifier for a PayPal account."""

    name: Optional[Name] = UNSET
    """The name of the party."""

    phone: Optional[PhoneWithType] = UNSET
    """The phone information."""

    birth_date: Optional[str] = UNSET
    """The stand-alone date, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. To
    represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone
    data. Whenever possible, use the standard ``date_time`` type. This regular expression does not validate all dates.
    For example, February 31 is valid and nothing is known about leap years."""

    tax_info: Optional[TaxInfo] = UNSET
    """The tax ID of the customer. The customer is also known as the payer. Both ``tax_id`` and ``tax_id_type`` are
    required."""

    address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""


class PayerDict(TypedDict):
    email_address: NotRequired[str]
    payer_id: NotRequired[str]
    name: NotRequired[Name | NameDict]
    phone: NotRequired[PhoneWithType | PhoneWithTypeDict]
    birth_date: NotRequired[str]
    tax_info: NotRequired[TaxInfo | TaxInfoDict]
    address: NotRequired[Address | AddressDict]
