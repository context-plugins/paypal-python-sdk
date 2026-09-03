from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.disbursement_mode import DisbursementModeOrStr
from .platform_fee import PlatformFee, PlatformFeeDict


class PaymentInstruction(SdkBaseModel):
    """Any additional payment instructions to be consider during payment processing. This processing instruction is
    applicable for Capturing an order or Authorizing an Order."""

    platform_fees: Optional[list[PlatformFee]] = UNSET
    """An array of various fees, commissions, tips, or donations. This field is only applicable to merchants that been
    enabled for PayPal Complete Payments Platform for Marketplaces and Platforms capability."""

    disbursement_mode: Optional[DisbursementModeOrStr] = UNSET
    """The funds that are held on behalf of the merchant."""

    payee_pricing_tier_id: Optional[str] = UNSET
    """This field is only enabled for selected merchants/partners to use and provides the ability to trigger a specific
    pricing rate/plan for a payment transaction. The list of eligible 'payee_pricing_tier_id' would be provided to you
    by your Account Manager. Specifying values other than the one provided to you by your account manager would result
    in an error."""

    payee_receivable_fx_rate_id: Optional[str] = UNSET
    """FX identifier generated returned by PayPal to be used for payment processing in order to honor FX rate (for
    eligible integrations) to be used when amount is settled/received into the payee account."""


class PaymentInstructionDict(TypedDict):
    platform_fees: NotRequired[list[PlatformFee | PlatformFeeDict]]
    disbursement_mode: NotRequired[DisbursementModeOrStr]
    payee_pricing_tier_id: NotRequired[str]
    payee_receivable_fx_rate_id: NotRequired[str]
