from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name import Name, NameDict
from .phone_with_type import PhoneWithType, PhoneWithTypeDict
from .shipping_details import ShippingDetails, ShippingDetailsDict
from .subscription_payment_source import SubscriptionPaymentSource, SubscriptionPaymentSourceDict


class SubscriberRequest(SdkBaseModel):
    """The subscriber request information ."""

    name: Optional[Name] = UNSET
    """The name of the party."""

    phone: Optional[PhoneWithType] = UNSET
    """The phone information."""

    shipping_address: Optional[ShippingDetails] = UNSET
    """The shipping details."""

    payment_source: Optional[SubscriptionPaymentSource] = UNSET
    """The payment source definition. To be eligible to create subscription using debit or credit card, you will need to
    sign up here (https://www.paypal.com/bizsignup/entry/product/ppcp). Please note, its available only for non-3DS
    cards and for merchants in US and AU regions."""


class SubscriberRequestDict(TypedDict):
    name: NotRequired[NameDict]
    phone: NotRequired[PhoneWithTypeDict]
    shipping_address: NotRequired[ShippingDetailsDict]
    payment_source: NotRequired[SubscriptionPaymentSourceDict]
