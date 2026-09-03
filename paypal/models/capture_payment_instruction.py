from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.disbursement_mode import DisbursementModeOrStr
from .platform_fee import PlatformFee, PlatformFeeDict


class CapturePaymentInstruction(SdkBaseModel):
    """Any additional payment instructions to be consider during payment processing. This processing instruction is
    applicable for Capturing an order or Authorizing an Order."""

    platform_fees: Optional[list[PlatformFee]] = UNSET
    """An array of platform or partner fees, commissions, or brokerage fees that associated with the captured
    payment."""

    disbursement_mode: Optional[DisbursementModeOrStr] = UNSET
    """The funds that are held on behalf of the merchant."""

    payee_receivable_fx_rate_id: Optional[str] = UNSET
    """FX identifier generated returned by PayPal to be used for payment processing in order to honor FX rate (for
    eligible integrations) to be used when amount is settled/received into the payee account."""


class CapturePaymentInstructionDict(TypedDict):
    platform_fees: NotRequired[list[PlatformFee | PlatformFeeDict]]
    disbursement_mode: NotRequired[DisbursementModeOrStr]
    payee_receivable_fx_rate_id: NotRequired[str]
