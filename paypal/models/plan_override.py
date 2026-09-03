from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_cycle_override import BillingCycleOverride, BillingCycleOverrideDict
from .payment_preferences_override import PaymentPreferencesOverride, PaymentPreferencesOverrideDict
from .taxes_override import TaxesOverride, TaxesOverrideDict


class PlanOverride(SdkBaseModel):
    """An inline plan object to customise the subscription. You can override plan level default attributes by providing
    customised values for the subscription in this object."""

    billing_cycles: Optional[list[BillingCycleOverride]] = UNSET
    """An array of billing cycles for trial billing and regular billing. The subscription billing cycle definition has
    to adhere to the plan billing cycle definition."""

    payment_preferences: Optional[PaymentPreferencesOverride] = UNSET
    """The payment preferences to override at subscription level."""

    taxes: Optional[TaxesOverride] = UNSET
    """The tax details."""


class PlanOverrideDict(TypedDict):
    billing_cycles: NotRequired[list[BillingCycleOverride | BillingCycleOverrideDict]]
    payment_preferences: NotRequired[PaymentPreferencesOverride | PaymentPreferencesOverrideDict]
    taxes: NotRequired[TaxesOverride | TaxesOverrideDict]
