from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .refund_payment_instruction import RefundPaymentInstruction, RefundPaymentInstructionDict


class RefundRequest(SdkBaseModel):
    """Refunds a captured payment, by ID. For a full refund, include an empty request body. For a partial refund,
    include an amount object in the request body."""

    amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    custom_id: Optional[str] = UNSET
    """The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal
    transactions. Appears in transaction and settlement reports. The pattern is defined by an external party and
    supports Unicode."""

    invoice_id: Optional[str] = UNSET
    """The API caller-provided external invoice ID for this order. The pattern is defined by an external party and
    supports Unicode."""

    note_to_payer: Optional[str] = UNSET
    """The reason for the refund. Appears in both the payer's transaction history and the emails that the payer
    receives. The pattern is defined by an external party and supports Unicode."""

    payment_instruction: Optional[RefundPaymentInstruction] = UNSET
    """Any additional payments instructions during refund payment processing. This object is only applicable to
    merchants that have been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability. Please
    speak to your account manager if you want to use this capability."""


class RefundRequestDict(TypedDict):
    amount: NotRequired[Money | MoneyDict]
    custom_id: NotRequired[str]
    invoice_id: NotRequired[str]
    note_to_payer: NotRequired[str]
    payment_instruction: NotRequired[RefundPaymentInstruction | RefundPaymentInstructionDict]
