from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.capture_status import CaptureStatusOrStr
from .subscription_amount_with_breakdown import SubscriptionAmountWithBreakdown, SubscriptionAmountWithBreakdownDict
from .subscription_payer_name import SubscriptionPayerName, SubscriptionPayerNameDict


class SubscriptionTransactionDetails(SdkBaseModel):
    """The transaction details."""

    status: Optional[CaptureStatusOrStr] = UNSET
    """The status of the captured payment."""

    id: str
    """The PayPal-generated transaction ID."""

    amount_with_breakdown: SubscriptionAmountWithBreakdown
    """The breakdown details for the amount. Includes the gross, tax, fee, and shipping amounts."""

    payer_name: Optional[SubscriptionPayerName] = UNSET
    """The name of the party."""

    payer_email: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    time: str
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""


class SubscriptionTransactionDetailsDict(TypedDict):
    status: NotRequired[CaptureStatusOrStr]
    id: str
    amount_with_breakdown: SubscriptionAmountWithBreakdown | SubscriptionAmountWithBreakdownDict
    payer_name: NotRequired[SubscriptionPayerName | SubscriptionPayerNameDict]
    payer_email: NotRequired[str]
    time: str
