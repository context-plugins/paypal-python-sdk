from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payment_initiator import PaymentInitiatorOrStr
from .enums.stored_payment_source_usage_type import StoredPaymentSourceUsageTypeOrStr
from .enums.usage_pattern import UsagePatternOrStr


class PayPalWalletStoredCredential(SdkBaseModel):
    """Provides additional details to process a payment using the PayPal wallet billing agreement or a vaulted payment
    method that has been stored or is intended to be stored."""

    payment_initiator: PaymentInitiatorOrStr
    """The person or party who initiated or triggered the payment."""

    charge_pattern: Optional[UsagePatternOrStr] = UNSET
    """DEPRECATED. Expected business/pricing model for the billing agreement, Please use usage_pattern instead."""

    usage_pattern: Optional[UsagePatternOrStr] = UNSET
    """Expected business/pricing model for the billing agreement."""

    usage: Optional[StoredPaymentSourceUsageTypeOrStr] = UNSET
    """Indicates if this is a ``first`` or ``subsequent`` payment using a stored payment source (also referred to as
    stored credential or card on file)."""


class PayPalWalletStoredCredentialDict(TypedDict):
    payment_initiator: PaymentInitiatorOrStr
    charge_pattern: NotRequired[UsagePatternOrStr]
    usage_pattern: NotRequired[UsagePatternOrStr]
    usage: NotRequired[StoredPaymentSourceUsageTypeOrStr]
