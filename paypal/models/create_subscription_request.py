from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .plan_override import PlanOverride, PlanOverrideDict
from .subscriber_request import SubscriberRequest, SubscriberRequestDict
from .subscription_application_context import SubscriptionApplicationContext, SubscriptionApplicationContextDict


class CreateSubscriptionRequest(SdkBaseModel):
    """The create subscription request details."""

    plan_id: str
    """The ID of the plan."""

    start_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    quantity: Optional[str] = UNSET
    """The quantity of the product in the subscription."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    subscriber: Optional[SubscriberRequest] = UNSET
    """The subscriber request information ."""

    auto_renewal: Optional[bool] = UNSET
    """DEPRECATED. Indicates whether the subscription auto-renews after the billing cycles complete."""

    application_context: Optional[SubscriptionApplicationContext] = UNSET
    """DEPRECATED. The application context, which customizes the payer experience during the subscription approval
    process with PayPal."""

    custom_id: Optional[str] = UNSET
    """The custom id for the subscription. Can be invoice id."""

    plan: Optional[PlanOverride] = UNSET
    """An inline plan object to customise the subscription. You can override plan level default attributes by providing
    customised values for the subscription in this object."""


class CreateSubscriptionRequestDict(TypedDict):
    plan_id: str
    start_time: NotRequired[str]
    quantity: NotRequired[str]
    shipping_amount: NotRequired[Money | MoneyDict]
    subscriber: NotRequired[SubscriberRequest | SubscriberRequestDict]
    auto_renewal: NotRequired[bool]
    application_context: NotRequired[SubscriptionApplicationContext | SubscriptionApplicationContextDict]
    custom_id: NotRequired[str]
    plan: NotRequired[PlanOverride | PlanOverrideDict]
