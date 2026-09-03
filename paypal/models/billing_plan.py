from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.subscription_plan_status import SubscriptionPlanStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .merchant_preferences import MerchantPreferences, MerchantPreferencesDict
from .payment_preferences import PaymentPreferences, PaymentPreferencesDict
from .subscription_billing_cycle import SubscriptionBillingCycle, SubscriptionBillingCycleDict
from .taxes import Taxes, TaxesDict


class BillingPlan(SdkBaseModel):
    """The plan details."""

    id: Optional[str] = UNSET
    """The unique PayPal-generated ID for the plan."""

    product_id: Optional[str] = UNSET
    """The ID for the product."""

    name: Optional[str] = UNSET
    """The plan name."""

    status: Optional[SubscriptionPlanStatusOrStr] = UNSET
    """The plan status."""

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

    create_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    update_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""


class BillingPlanDict(TypedDict):
    id: NotRequired[str]
    product_id: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[SubscriptionPlanStatusOrStr]
    description: NotRequired[str]
    billing_cycles: NotRequired[list[SubscriptionBillingCycle | SubscriptionBillingCycleDict]]
    payment_preferences: NotRequired[PaymentPreferences | PaymentPreferencesDict]
    merchant_preferences: NotRequired[MerchantPreferences | MerchantPreferencesDict]
    taxes: NotRequired[Taxes | TaxesDict]
    quantity_supported: NotRequired[bool]
    create_time: NotRequired[str]
    update_time: NotRequired[str]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
