from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name import Name, NameDict
from .shipping_details import ShippingDetails, ShippingDetailsDict
from .subscription_payment_source_response import (
    SubscriptionPaymentSourceResponse,
    SubscriptionPaymentSourceResponseDict,
)


class Subscriber(SdkBaseModel):
    """The subscriber response information."""

    name: Optional[Name] = UNSET
    """The name of the party."""

    shipping_address: Optional[ShippingDetails] = UNSET
    """The shipping details."""

    payment_source: Optional[SubscriptionPaymentSourceResponse] = UNSET
    """The payment source used to fund the payment."""


class SubscriberDict(TypedDict):
    name: NotRequired[NameDict]
    shipping_address: NotRequired[ShippingDetailsDict]
    payment_source: NotRequired[SubscriptionPaymentSourceResponseDict]
