from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_card import ApplePayCard, ApplePayCardDict


class ApplePayPaymentToken(SdkBaseModel):
    """A resource representing a response for Apple Pay."""

    card: Optional[ApplePayCard] = UNSET
    """The payment card to be used to fund a payment. Can be a credit or debit card."""


class ApplePayPaymentTokenDict(TypedDict):
    card: NotRequired[ApplePayCard | ApplePayCardDict]
