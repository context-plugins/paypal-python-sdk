from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_request import ApplePayRequest, ApplePayRequestDict
from .card_request import CardRequest, CardRequestDict
from .google_pay_request import GooglePayRequest, GooglePayRequestDict
from .pay_pal_wallet import PayPalWallet, PayPalWalletDict
from .token import Token, TokenDict
from .venmo_wallet_request import VenmoWalletRequest, VenmoWalletRequestDict


class OrderCaptureRequestPaymentSource(SdkBaseModel):
    """The payment source definition."""

    card: Optional[CardRequest] = UNSET
    """The payment card to use to fund a payment. Can be a credit or debit card. Note: Passing card number, cvv and
    expiry directly via the API requires PCI SAQ D compliance. *PayPal offers a mechanism by which you do not have to
    take on the PCI SAQ D burden by using hosted fields - refer to this Integration Guide*."""

    token: Optional[Token] = UNSET
    """The tokenized payment source to fund a payment."""

    paypal: Optional[PayPalWallet] = UNSET
    """A resource that identifies a PayPal Wallet is used for payment."""

    apple_pay: Optional[ApplePayRequest] = UNSET
    """Information needed to pay using ApplePay."""

    google_pay: Optional[GooglePayRequest] = UNSET
    """Information needed to pay using Google Pay."""

    venmo: Optional[VenmoWalletRequest] = UNSET
    """Information needed to pay using Venmo."""


class OrderCaptureRequestPaymentSourceDict(TypedDict):
    card: NotRequired[CardRequest | CardRequestDict]
    token: NotRequired[Token | TokenDict]
    paypal: NotRequired[PayPalWallet | PayPalWalletDict]
    apple_pay: NotRequired[ApplePayRequest | ApplePayRequestDict]
    google_pay: NotRequired[GooglePayRequest | GooglePayRequestDict]
    venmo: NotRequired[VenmoWalletRequest | VenmoWalletRequestDict]
