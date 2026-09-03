from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription_card_request import SubscriptionCardRequest, SubscriptionCardRequestDict


class SubscriptionPaymentSource(SdkBaseModel):
    """The payment source definition. To be eligible to create subscription using debit or credit card, you will need to
    sign up here (https://www.paypal.com/bizsignup/entry/product/ppcp). Please note, its available only for non-3DS
    cards and for merchants in US and AU regions."""

    card: Optional[SubscriptionCardRequest] = UNSET
    """The payment card to use to fund a payment. Can be a credit or debit card."""


class SubscriptionPaymentSourceDict(TypedDict):
    card: NotRequired[SubscriptionCardRequest | SubscriptionCardRequestDict]
