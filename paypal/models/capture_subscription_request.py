from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.capture_type import CaptureTypeOrStr
from .money import Money, MoneyDict


class CaptureSubscriptionRequest(SdkBaseModel):
    """The charge amount from the subscriber."""

    note: str
    """The reason or note for the subscription charge."""

    capture_type: CaptureTypeOrStr
    """The type of capture."""

    amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class CaptureSubscriptionRequestDict(TypedDict):
    note: str
    capture_type: CaptureTypeOrStr
    amount: Money | MoneyDict
