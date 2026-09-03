from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_payment_token import ApplePayPaymentToken, ApplePayPaymentTokenDict
from .card_payment_token_entity import CardPaymentTokenEntity, CardPaymentTokenEntityDict
from .pay_pal_payment_token import PayPalPaymentToken, PayPalPaymentTokenDict
from .venmo_payment_token import VenmoPaymentToken, VenmoPaymentTokenDict


class PaymentTokenResponsePaymentSource(SdkBaseModel):
    """The vaulted payment method details."""

    card: Optional[CardPaymentTokenEntity] = UNSET
    """Full representation of a Card Payment Token including network token."""

    paypal: Optional[PayPalPaymentToken] = UNSET
    """Full representation of a PayPal Payment Token."""

    venmo: Optional[VenmoPaymentToken] = UNSET
    """Full representation of a Venmo Payment Token."""

    apple_pay: Optional[ApplePayPaymentToken] = UNSET
    """A resource representing a response for Apple Pay."""


class PaymentTokenResponsePaymentSourceDict(TypedDict):
    card: NotRequired[CardPaymentTokenEntity | CardPaymentTokenEntityDict]
    paypal: NotRequired[PayPalPaymentToken | PayPalPaymentTokenDict]
    venmo: NotRequired[VenmoPaymentToken | VenmoPaymentTokenDict]
    apple_pay: NotRequired[ApplePayPaymentToken | ApplePayPaymentTokenDict]
