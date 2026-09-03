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

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    payer_id: Optional[str] = UNSET
    """The account identifier for a PayPal account."""

    name: Optional[Name] = UNSET
    """The name of the party."""

    shipping_address: Optional[ShippingDetails] = UNSET
    """The shipping details."""

    payment_source: Optional[SubscriptionPaymentSourceResponse] = UNSET
    """The payment source used to fund the payment."""


class SubscriberDict(TypedDict):
    email_address: NotRequired[str]
    payer_id: NotRequired[str]
    name: NotRequired[Name | NameDict]
    shipping_address: NotRequired[ShippingDetails | ShippingDetailsDict]
    payment_source: NotRequired[SubscriptionPaymentSourceResponse | SubscriptionPaymentSourceResponseDict]
