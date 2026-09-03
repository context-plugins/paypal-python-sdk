from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pay_pal_payment_token_customer_type import PayPalPaymentTokenCustomerTypeOrStr
from .enums.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageTypeOrStr
from .enums.usage_pattern import UsagePatternOrStr
from .vaulted_digital_wallet_shipping_details import (
    VaultedDigitalWalletShippingDetails,
    VaultedDigitalWalletShippingDetailsDict,
)
from .venmo_experience_context import VenmoExperienceContext, VenmoExperienceContextDict


class VaultVenmoRequest(SdkBaseModel):
    """A resource representing a request to vault Venmo."""

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

    experience_context: Optional[VenmoExperienceContext] = UNSET
    """A resource representing an experience context of vault a venmo account."""


class VaultVenmoRequestDict(TypedDict):
    description: NotRequired[str]
    usage_pattern: NotRequired[UsagePatternOrStr]
    shipping: NotRequired[VaultedDigitalWalletShippingDetails | VaultedDigitalWalletShippingDetailsDict]
    permit_multiple_payment_tokens: NotRequired[bool]
    usage_type: NotRequired[PayPalPaymentTokenUsageTypeOrStr]
    customer_type: NotRequired[PayPalPaymentTokenCustomerTypeOrStr]
    experience_context: NotRequired[VenmoExperienceContext | VenmoExperienceContextDict]
