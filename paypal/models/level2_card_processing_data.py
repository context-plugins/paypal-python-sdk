from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class Level2CardProcessingData(SdkBaseModel):
    """The level 2 card processing data collections. If your merchant account has been configured for Level 2 processing
    this field will be passed to the processor on your behalf. Please contact your PayPal Technical Account Manager to
    define level 2 data for your business."""

    invoice_id: Optional[str] = UNSET
    """Use this field to pass a purchase identification value of up to 127 ASCII characters. The length of this field
    will be adjusted to meet network specifications (25chars for Visa and Mastercard, 17chars for Amex), and the
    original invoice ID will still be displayed in your existing reports."""

    tax_total: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class Level2CardProcessingDataDict(TypedDict):
    invoice_id: NotRequired[str]
    tax_total: NotRequired[Money | MoneyDict]
