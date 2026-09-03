from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cycle_execution import CycleExecution, CycleExecutionDict
from .failed_payment_details import FailedPaymentDetails, FailedPaymentDetailsDict
from .last_payment_details import LastPaymentDetails, LastPaymentDetailsDict
from .money import Money, MoneyDict


class SubscriptionBillingInformation(SdkBaseModel):
    """The billing details for the subscription. If the subscription was or is active, these fields are populated."""

    outstanding_balance: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    cycle_executions: Optional[list[CycleExecution]] = UNSET
    """The trial and regular billing executions."""

    last_payment: Optional[LastPaymentDetails] = UNSET
    """The details for the last payment."""

    next_billing_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    final_payment_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    failed_payments_count: int
    """The number of consecutive payment failures. Resets to ``0`` after a successful payment. If this reaches the
    ``payment_failure_threshold`` value, the subscription updates to the ``SUSPENDED`` state."""

    last_failed_payment: Optional[FailedPaymentDetails] = UNSET
    """The details for the failed payment of the subscription."""


class SubscriptionBillingInformationDict(TypedDict):
    outstanding_balance: Money | MoneyDict
    cycle_executions: NotRequired[list[CycleExecution | CycleExecutionDict]]
    last_payment: NotRequired[LastPaymentDetails | LastPaymentDetailsDict]
    next_billing_time: NotRequired[str]
    final_payment_time: NotRequired[str]
    failed_payments_count: int
    last_failed_payment: NotRequired[FailedPaymentDetails | FailedPaymentDetailsDict]
