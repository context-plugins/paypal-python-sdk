from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.plan_request_status import PlanRequestStatusOrStr
from .merchant_preferences import MerchantPreferences, MerchantPreferencesDict
from .payment_preferences import PaymentPreferences, PaymentPreferencesDict
from .subscription_billing_cycle import SubscriptionBillingCycle, SubscriptionBillingCycleDict
from .taxes import Taxes, TaxesDict


class PlanRequest(SdkBaseModel):
    """The create plan request details."""

    product_id: str
    """The ID of the product created through Catalog Products API."""

    name: str
    """The plan name."""

    status: Optional[PlanRequestStatusOrStr] = UNSET
    """The initial state of the plan. Allowed input values are CREATED and ACTIVE."""

    description: Optional[str] = UNSET
    """The detailed description of the plan."""

    billing_cycles: list[SubscriptionBillingCycle]
    """An array of billing cycles for trial billing and regular billing. A plan can have at most two trial cycles and
    only one regular cycle."""

    payment_preferences: PaymentPreferences
    """The payment preferences for a subscription."""

    merchant_preferences: Optional[MerchantPreferences] = UNSET
    """The merchant preferences for a subscription."""

    taxes: Optional[Taxes] = UNSET
    """The tax details."""

    quantity_supported: Optional[bool] = UNSET
    """Indicates whether you can subscribe to this plan by providing a quantity for the goods or service."""


class PlanRequestDict(TypedDict):
    product_id: str
    name: str
    status: NotRequired[PlanRequestStatusOrStr]
    description: NotRequired[str]
    billing_cycles: list[SubscriptionBillingCycle | SubscriptionBillingCycleDict]
    payment_preferences: PaymentPreferences | PaymentPreferencesDict
    merchant_preferences: NotRequired[MerchantPreferences | MerchantPreferencesDict]
    taxes: NotRequired[Taxes | TaxesDict]
    quantity_supported: NotRequired[bool]
