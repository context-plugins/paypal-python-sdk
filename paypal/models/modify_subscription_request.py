from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .plan_override import PlanOverride, PlanOverrideDict
from .shipping_details import ShippingDetails, ShippingDetailsDict
from .subscription_patch_application_context import (
    SubscriptionPatchApplicationContext,
    SubscriptionPatchApplicationContextDict,
)


class ModifySubscriptionRequest(SdkBaseModel):
    """The request to update the quantity of the product or service in a subscription. You can also use this method to
    switch the plan and update the ``shipping_amount`` and ``shipping_address`` values for the subscription. This type
    of update requires the buyer's consent."""

    plan_id: Optional[str] = UNSET
    """The unique PayPal-generated ID for the plan."""

    quantity: Optional[str] = UNSET
    """The quantity of the product or service in the subscription."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_address: Optional[ShippingDetails] = UNSET
    """The shipping details."""

    application_context: Optional[SubscriptionPatchApplicationContext] = UNSET
    """The application context, which customizes the payer experience during the subscription approval process with
    PayPal."""

    plan: Optional[PlanOverride] = UNSET
    """An inline plan object to customise the subscription. You can override plan level default attributes by providing
    customised values for the subscription in this object."""


class ModifySubscriptionRequestDict(TypedDict):
    plan_id: NotRequired[str]
    quantity: NotRequired[str]
    shipping_amount: NotRequired[Money | MoneyDict]
    shipping_address: NotRequired[ShippingDetails | ShippingDetailsDict]
    application_context: NotRequired[SubscriptionPatchApplicationContext | SubscriptionPatchApplicationContextDict]
    plan: NotRequired[PlanOverride | PlanOverrideDict]
