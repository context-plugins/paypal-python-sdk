from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pay_pal_payment_token_customer_type import PayPalPaymentTokenCustomerTypeOrStr
from .enums.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageTypeOrStr
from .enums.store_in_vault_instruction import StoreInVaultInstructionOrStr
from .enums.usage_pattern import UsagePatternOrStr


class PayPalWalletVaultInstruction(SdkBaseModel):
    store_in_vault: Optional[StoreInVaultInstructionOrStr] = UNSET
    """Defines how and when the payment source gets vaulted."""

    description: Optional[str] = UNSET
    """The description displayed to PayPal consumer on the approval flow for PayPal, as well as on the PayPal payment
    token management experience on PayPal.com."""

    usage_pattern: Optional[UsagePatternOrStr] = UNSET
    """Expected business/pricing model for the billing agreement."""

    usage_type: PayPalPaymentTokenUsageTypeOrStr
    """The usage type associated with the PayPal payment token."""

    customer_type: Optional[PayPalPaymentTokenCustomerTypeOrStr] = UNSET
    """The customer type associated with the PayPal payment token. This is to indicate whether the customer acting on
    the merchant / platform is either a business or a consumer."""

    permit_multiple_payment_tokens: Optional[bool] = UNSET
    """Create multiple payment tokens for the same payer, merchant/platform combination. Use this when the customer has
    not logged in at merchant/platform. The payment token thus generated, can then also be used to create the customer
    account at merchant/platform. Use this also when multiple payment tokens are required for the same payer, different
    customer at merchant/platform. This helps to identify customers distinctly even though they may share the same
    PayPal account. This only applies to PayPal payment source."""


class PayPalWalletVaultInstructionDict(TypedDict):
    store_in_vault: NotRequired[StoreInVaultInstructionOrStr]
    description: NotRequired[str]
    usage_pattern: NotRequired[UsagePatternOrStr]
    usage_type: PayPalPaymentTokenUsageTypeOrStr
    customer_type: NotRequired[PayPalPaymentTokenCustomerTypeOrStr]
    permit_multiple_payment_tokens: NotRequired[bool]
