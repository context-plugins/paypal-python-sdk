from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_cycle import BillingCycle, BillingCycleDict
from .one_time_charge import OneTimeCharge, OneTimeChargeDict


class Plan(SdkBaseModel):
    """The merchant level Recurring Billing plan metadata for the Billing Agreement."""

    billing_cycles: list[BillingCycle]
    """An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and
    only one regular cycle."""

    one_time_charges: OneTimeCharge
    """The one-time charge info at the time of checkout."""

    name: Optional[str] = UNSET
    """Name of the recurring plan."""


class PlanDict(TypedDict):
    billing_cycles: list[BillingCycle | BillingCycleDict]
    one_time_charges: OneTimeCharge | OneTimeChargeDict
    name: NotRequired[str]
