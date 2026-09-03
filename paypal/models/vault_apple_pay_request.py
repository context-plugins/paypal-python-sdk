from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_request_card import ApplePayRequestCard, ApplePayRequestCardDict


class VaultApplePayRequest(SdkBaseModel):
    """A resource representing a request to vault Apple Pay."""

    token: Optional[str] = UNSET
    """Encrypted Apple Pay token, containing card information. This token would be base64 encoded."""

    card: Optional[ApplePayRequestCard] = UNSET
    """The payment card to be used to fund a payment. Can be a credit or debit card."""


class VaultApplePayRequestDict(TypedDict):
    token: NotRequired[str]
    card: NotRequired[ApplePayRequestCard | ApplePayRequestCardDict]
