from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_cycle import BillingCycle, BillingCycleDict
from .money import Money, MoneyDict


class OrderBillingPlan(SdkBaseModel):
    """Metadata for merchant-managed recurring billing plans. Valid only during the saved payment method token or
    billing agreement creation."""

    billing_cycles: list[BillingCycle]
    """An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and
    only one regular cycle."""

    setup_fee: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    name: Optional[str] = UNSET
    """Name of the recurring plan."""


class OrderBillingPlanDict(TypedDict):
    billing_cycles: list[BillingCycle | BillingCycleDict]
    setup_fee: NotRequired[Money | MoneyDict]
    name: NotRequired[str]
