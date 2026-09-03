from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict
from .money import Money, MoneyDict
from .plan_override import PlanOverride, PlanOverrideDict
from .shipping_details import ShippingDetails, ShippingDetailsDict


class ModifySubscriptionResponse(SdkBaseModel):
    """The response to a request to update the quantity of the product or service in a subscription. You can also use
    this method to switch the plan and update the ``shipping_amount`` and ``shipping_address`` values for the
    subscription. This type of update requires the buyer's consent."""

    plan_id: Optional[str] = UNSET
    """The unique PayPal-generated ID for the plan."""

    quantity: Optional[str] = UNSET
    """The quantity of the product or service in the subscription."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_address: Optional[ShippingDetails] = UNSET
    """The shipping details."""

    plan: Optional[PlanOverride] = UNSET
    """An inline plan object to customise the subscription. You can override plan level default attributes by providing
    customised values for the subscription in this object."""

    plan_overridden: Optional[bool] = UNSET
    """Indicates whether the subscription has overridden any plan attributes."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""


class ModifySubscriptionResponseDict(TypedDict):
    plan_id: NotRequired[str]
    quantity: NotRequired[str]
    shipping_amount: NotRequired[Money | MoneyDict]
    shipping_address: NotRequired[ShippingDetails | ShippingDetailsDict]
    plan: NotRequired[PlanOverride | PlanOverrideDict]
    plan_overridden: NotRequired[bool]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
