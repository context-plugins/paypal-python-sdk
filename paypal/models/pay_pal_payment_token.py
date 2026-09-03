from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.pay_pal_payment_token_customer_type import PayPalPaymentTokenCustomerTypeOrStr
from .enums.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageTypeOrStr
from .enums.usage_pattern import UsagePatternOrStr
from .name import Name, NameDict
from .phone import Phone, PhoneDict
from .phone_with_type import PhoneWithType, PhoneWithTypeDict
from .vaulted_digital_wallet_shipping_details import (
    VaultedDigitalWalletShippingDetails,
    VaultedDigitalWalletShippingDetailsDict,
)


class PayPalPaymentToken(SdkBaseModel):
    """Full representation of a PayPal Payment Token."""

    description: Optional[str] = UNSET
    """The description displayed to the consumer on the approval flow for a digital wallet, as well as on the merchant
    view of the payment token management experience. exp: PayPal.com."""

    usage_pattern: Optional[UsagePatternOrStr] = UNSET
    """Expected business/charge model for the billing agreement."""

    shipping: Optional[VaultedDigitalWalletShippingDetails] = UNSET
    """The shipping details."""

    permit_multiple_payment_tokens: Optional[bool] = UNSET
    """Create multiple payment tokens for the same payer, merchant/platform combination. Use this when the customer has
    not logged in at merchant/platform. The payment token thus generated, can then also be used to create the customer
    account at merchant/platform. Use this also when multiple payment tokens are required for the same payer, different
    customer at merchant/platform. This helps to identify customers distinctly even though they may share the same
    PayPal account. This only applies to PayPal payment source."""

    usage_type: Optional[PayPalPaymentTokenUsageTypeOrStr] = UNSET
    """The usage type associated with a digital wallet payment token."""

    customer_type: Optional[PayPalPaymentTokenCustomerTypeOrStr] = UNSET
    """The customer type associated with a digital wallet payment token. This is to indicate whether the customer acting
    on the merchant / platform is either a business or a consumer."""

    email_address: Optional[str] = UNSET
    """The internationalized email address.<blockquote><strong>Note:</strong> Up to 64 characters are allowed before and
    255 characters are allowed after the <code>@</code> sign. However, the generally accepted maximum length for an
    email address is 254 characters. The pattern verifies that an unquoted <code>@</code> sign exists.</blockquote>"""

    payer_id: Optional[str] = UNSET
    """The account identifier for a PayPal account."""

    name: Optional[Name] = UNSET
    """The name of the party."""

    phone: Optional[PhoneWithType] = UNSET
    """The phone information."""

    address: Optional[Address] = UNSET
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    account_id: Optional[str] = UNSET
    """The account identifier for a PayPal account."""

    phone_number: Optional[Phone] = UNSET
    """The phone number, in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""


class PayPalPaymentTokenDict(TypedDict):
    description: NotRequired[str]
    usage_pattern: NotRequired[UsagePatternOrStr]
    shipping: NotRequired[VaultedDigitalWalletShippingDetails | VaultedDigitalWalletShippingDetailsDict]
    permit_multiple_payment_tokens: NotRequired[bool]
    usage_type: NotRequired[PayPalPaymentTokenUsageTypeOrStr]
    customer_type: NotRequired[PayPalPaymentTokenCustomerTypeOrStr]
    email_address: NotRequired[str]
    payer_id: NotRequired[str]
    name: NotRequired[Name | NameDict]
    phone: NotRequired[PhoneWithType | PhoneWithTypeDict]
    address: NotRequired[Address | AddressDict]
    account_id: NotRequired[str]
    phone_number: NotRequired[Phone | PhoneDict]
