from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .name import Name, NameDict
from .pay_pal_wallet_attributes import PayPalWalletAttributes, PayPalWalletAttributesDict
from .pay_pal_wallet_experience_context import PayPalWalletExperienceContext, PayPalWalletExperienceContextDict
from .pay_pal_wallet_stored_credential import PayPalWalletStoredCredential, PayPalWalletStoredCredentialDict
from .phone_with_type import PhoneWithType, PhoneWithTypeDict
from .tax_info import TaxInfo, TaxInfoDict


class PayPalWallet(SdkBaseModel):
    """A resource that identifies a PayPal Wallet is used for payment."""

    vault_id: Optional[str] = UNSET
    """The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the
    saved payment source can be used for future transactions."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

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

    attributes: Optional[PayPalWalletAttributes] = UNSET
    """Additional attributes associated with the use of this PayPal Wallet."""

    experience_context: Optional[PayPalWalletExperienceContext] = UNSET
    """Customizes the payer experience during the approval process for payment with PayPal. Note: Partners and
    Marketplaces might configure brand_name and shipping_preference during partner account setup, which overrides the
    request values."""

    billing_agreement_id: Optional[str] = UNSET
    """The PayPal billing agreement ID. References an approved recurring payment for goods or services."""

    stored_credential: Optional[PayPalWalletStoredCredential] = UNSET
    """Provides additional details to process a payment using the PayPal wallet billing agreement or a vaulted payment
    method that has been stored or is intended to be stored."""


class PayPalWalletDict(TypedDict):
    vault_id: NotRequired[str]
    email_address: NotRequired[str]
    name: NotRequired[Name | NameDict]
    phone: NotRequired[PhoneWithType | PhoneWithTypeDict]
    birth_date: NotRequired[str]
    tax_info: NotRequired[TaxInfo | TaxInfoDict]
    address: NotRequired[Address | AddressDict]
    attributes: NotRequired[PayPalWalletAttributes | PayPalWalletAttributesDict]
    experience_context: NotRequired[PayPalWalletExperienceContext | PayPalWalletExperienceContextDict]
    billing_agreement_id: NotRequired[str]
    stored_credential: NotRequired[PayPalWalletStoredCredential | PayPalWalletStoredCredentialDict]
