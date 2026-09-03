from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict
from .money import Money, MoneyDict
from .plan_details import PlanDetails, PlanDetailsDict
from .subscriber import Subscriber, SubscriberDict
from .subscription_billing_information import SubscriptionBillingInformation, SubscriptionBillingInformationDict


class Subscription(SdkBaseModel):
    """The subscription details."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the subscription."""

    plan_id: Optional[str] = UNSET
    """The ID of the plan."""

    start_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    quantity: Optional[str] = UNSET
    """The quantity of the product in the subscription."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    subscriber: Optional[Subscriber] = UNSET
    """The subscriber response information."""

    billing_info: Optional[SubscriptionBillingInformation] = UNSET
    """The billing details for the subscription. If the subscription was or is active, these fields are populated."""

    create_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    update_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    custom_id: Optional[str] = UNSET
    """The custom id for the subscription. Can be invoice id."""

    plan_overridden: Optional[bool] = UNSET
    """Indicates whether the subscription has overridden any plan attributes."""

    plan: Optional[PlanDetails] = UNSET
    """The plan details."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""


class SubscriptionDict(TypedDict):
    id: NotRequired[str]
    plan_id: NotRequired[str]
    start_time: NotRequired[str]
    quantity: NotRequired[str]
    shipping_amount: NotRequired[Money | MoneyDict]
    subscriber: NotRequired[Subscriber | SubscriberDict]
    billing_info: NotRequired[SubscriptionBillingInformation | SubscriptionBillingInformationDict]
    create_time: NotRequired[str]
    update_time: NotRequired[str]
    custom_id: NotRequired[str]
    plan_overridden: NotRequired[bool]
    plan: NotRequired[PlanDetails | PlanDetailsDict]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
