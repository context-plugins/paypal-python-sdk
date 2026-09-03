from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .merchant_preferences import MerchantPreferences, MerchantPreferencesDict
from .payment_preferences import PaymentPreferences, PaymentPreferencesDict
from .subscription_billing_cycle import SubscriptionBillingCycle, SubscriptionBillingCycleDict
from .taxes import Taxes, TaxesDict


class PlanDetails(SdkBaseModel):
    """The plan details."""

    product_id: Optional[str] = UNSET
    """The ID for the product."""

    name: Optional[str] = UNSET
    """The plan name."""

    description: Optional[str] = UNSET
    """The detailed description of the plan."""

    billing_cycles: Optional[list[SubscriptionBillingCycle]] = UNSET
    """An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and
    only one regular cycle."""

    payment_preferences: Optional[PaymentPreferences] = UNSET
    """The payment preferences for a subscription."""

    merchant_preferences: Optional[MerchantPreferences] = UNSET
    """The merchant preferences for a subscription."""

    taxes: Optional[Taxes] = UNSET
    """The tax details."""

    quantity_supported: Optional[bool] = UNSET
    """Indicates whether you can subscribe to this plan by providing a quantity for the goods or service."""


class PlanDetailsDict(TypedDict):
    product_id: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    billing_cycles: NotRequired[list[SubscriptionBillingCycle | SubscriptionBillingCycleDict]]
    payment_preferences: NotRequired[PaymentPreferences | PaymentPreferencesDict]
    merchant_preferences: NotRequired[MerchantPreferences | MerchantPreferencesDict]
    taxes: NotRequired[Taxes | TaxesDict]
    quantity_supported: NotRequired[bool]
