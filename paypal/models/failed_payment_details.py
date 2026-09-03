from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reason_code import ReasonCodeOrStr
from .money import Money, MoneyDict


class FailedPaymentDetails(SdkBaseModel):
    """The details for the failed payment of the subscription."""

    amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    time: str
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    reason_code: Optional[ReasonCodeOrStr] = UNSET
    """The reason code for the payment failure."""

    next_payment_retry_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""


class FailedPaymentDetailsDict(TypedDict):
    amount: Money | MoneyDict
    time: str
    reason_code: NotRequired[ReasonCodeOrStr]
    next_payment_retry_time: NotRequired[str]
