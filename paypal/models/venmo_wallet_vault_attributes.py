from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.store_in_vault_instruction import StoreInVaultInstructionOrStr
from .enums.venmo_payment_token_customer_type import VenmoPaymentTokenCustomerTypeOrStr
from .enums.venmo_payment_token_usage_pattern import VenmoPaymentTokenUsagePatternOrStr
from .enums.venmo_payment_token_usage_type import VenmoPaymentTokenUsageTypeOrStr


class VenmoWalletVaultAttributes(SdkBaseModel):
    """Resource consolidating common request and response attirbutes for vaulting Venmo Wallet."""

    store_in_vault: StoreInVaultInstructionOrStr
    """Defines how and when the payment source gets vaulted."""

    description: Optional[str] = UNSET
    """The description displayed to Venmo consumer on the approval flow for Venmo, as well as on the Venmo payment token
    management experience on Venmo.com."""

    usage_pattern: Optional[VenmoPaymentTokenUsagePatternOrStr] = UNSET
    """Expected business/pricing model for the billing agreement."""

    usage_type: VenmoPaymentTokenUsageTypeOrStr
    """The usage type associated with the Venmo payment token."""

    customer_type: Optional[VenmoPaymentTokenCustomerTypeOrStr] = UNSET
    """The customer type associated with the Venmo payment token. This is to indicate whether the customer acting on the
    merchant / platform is either a business or a consumer."""

    permit_multiple_payment_tokens: Optional[bool] = UNSET
    """Create multiple payment tokens for the same payer, merchant/platform combination. Use this when the customer has
    not logged in at merchant/platform. The payment token thus generated, can then also be used to create the customer
    account at merchant/platform. Use this also when multiple payment tokens are required for the same payer, different
    customer at merchant/platform. This helps to identify customers distinctly even though they may share the same Venmo
    account."""


class VenmoWalletVaultAttributesDict(TypedDict):
    store_in_vault: StoreInVaultInstructionOrStr
    description: NotRequired[str]
    usage_pattern: NotRequired[VenmoPaymentTokenUsagePatternOrStr]
    usage_type: VenmoPaymentTokenUsageTypeOrStr
    customer_type: NotRequired[VenmoPaymentTokenCustomerTypeOrStr]
    permit_multiple_payment_tokens: NotRequired[bool]
