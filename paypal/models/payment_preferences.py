from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.setup_fee_failure_action import SetupFeeFailureActionOrStr
from .money import Money, MoneyDict


class PaymentPreferences(SdkBaseModel):
    """The payment preferences for a subscription."""

    auto_bill_outstanding: Optional[bool] = UNSET
    """Indicates whether to automatically bill the outstanding amount in the next billing cycle."""

    setup_fee: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    setup_fee_failure_action: Optional[SetupFeeFailureActionOrStr] = UNSET
    """The action to take on the subscription if the initial payment for the setup fails."""

    payment_failure_threshold: Optional[int] = UNSET
    """The maximum number of payment failures before a subscription is suspended. For example, if
    ``payment_failure_threshold`` is ``2``, the subscription automatically updates to the ``SUSPEND`` state if two
    consecutive payments fail."""


class PaymentPreferencesDict(TypedDict):
    auto_bill_outstanding: NotRequired[bool]
    setup_fee: NotRequired[Money | MoneyDict]
    setup_fee_failure_action: NotRequired[SetupFeeFailureActionOrStr]
    payment_failure_threshold: NotRequired[int]
