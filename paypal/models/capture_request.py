from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capture_payment_instruction import CapturePaymentInstruction, CapturePaymentInstructionDict
from .money import Money, MoneyDict


class CaptureRequest(SdkBaseModel):
    """Captures either a portion or the full authorized amount of an authorized payment."""

    amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    invoice_id: Optional[str] = UNSET
    """The API caller-provided external invoice number for this order. Appears in both the payer's transaction history
    and the emails that the payer receives."""

    final_capture: Optional[bool] = UNSET
    """Indicates whether you can make additional captures against the authorized payment. Set to ``true`` if you do not
    intend to capture additional payments against the authorization. Set to ``false`` if you intend to capture
    additional payments against the authorization."""

    payment_instruction: Optional[CapturePaymentInstruction] = UNSET
    """Any additional payment instructions to be consider during payment processing. This processing instruction is
    applicable for Capturing an order or Authorizing an Order."""

    note_to_payer: Optional[str] = UNSET
    """An informational note about this settlement. Appears in both the payer's transaction history and the emails that
    the payer receives."""

    soft_descriptor: Optional[str] = UNSET
    """The payment descriptor on the payer's account statement."""


class CaptureRequestDict(TypedDict):
    amount: NotRequired[Money | MoneyDict]
    invoice_id: NotRequired[str]
    final_capture: NotRequired[bool]
    payment_instruction: NotRequired[CapturePaymentInstruction | CapturePaymentInstructionDict]
    note_to_payer: NotRequired[str]
    soft_descriptor: NotRequired[str]
