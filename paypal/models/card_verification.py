from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.orders_card_verification_method import OrdersCardVerificationMethod, OrdersCardVerificationMethodOrStr


class CardVerification(SdkBaseModel):
    """The API caller can opt in to verify the card through PayPal offered verification services (e.g. Smart Dollar
    Auth, 3DS)."""

    method: OrdersCardVerificationMethodOrStr = OrdersCardVerificationMethod.SCA_WHEN_REQUIRED
    """The method used for card verification."""


class CardVerificationDict(TypedDict):
    method: NotRequired[OrdersCardVerificationMethodOrStr]
