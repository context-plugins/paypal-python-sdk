from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .refund_platform_fee import RefundPlatformFee, RefundPlatformFeeDict


class RefundPaymentInstruction(SdkBaseModel):
    """Any additional payments instructions during refund payment processing. This object is only applicable to
    merchants that have been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability. Please
    speak to your account manager if you want to use this capability."""

    platform_fees: Optional[list[RefundPlatformFee]] = UNSET
    """Specifies the amount that the API caller will contribute to the refund being processed. The amount needs to be
    lower than platform_fees amount originally captured or the amount that is remaining if multiple refunds have been
    processed. This field is only applicable to merchants that have been enabled for PayPal Commerce Platform for
    Marketplaces and Platforms capability. Please speak to your account manager if you want to use this capability."""


class RefundPaymentInstructionDict(TypedDict):
    platform_fees: NotRequired[list[RefundPlatformFee | RefundPlatformFeeDict]]
