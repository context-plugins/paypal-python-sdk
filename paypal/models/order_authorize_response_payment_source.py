from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_payment_object import ApplePayPaymentObject, ApplePayPaymentObjectDict
from .card_response import CardResponse, CardResponseDict
from .google_pay_wallet_response import GooglePayWalletResponse, GooglePayWalletResponseDict
from .pay_pal_wallet_response import PayPalWalletResponse, PayPalWalletResponseDict
from .venmo_wallet_response import VenmoWalletResponse, VenmoWalletResponseDict


class OrderAuthorizeResponsePaymentSource(SdkBaseModel):
    """The payment source used to fund the payment."""

    card: Optional[CardResponse] = UNSET
    """The payment card to use to fund a payment. Card can be a credit or debit card."""

    paypal: Optional[PayPalWalletResponse] = UNSET
    """The PayPal Wallet response."""

    apple_pay: Optional[ApplePayPaymentObject] = UNSET
    """Information needed to pay using ApplePay."""

    google_pay: Optional[GooglePayWalletResponse] = UNSET
    """Google Pay Wallet payment data."""

    venmo: Optional[VenmoWalletResponse] = UNSET
    """Venmo wallet response."""


class OrderAuthorizeResponsePaymentSourceDict(TypedDict):
    card: NotRequired[CardResponse | CardResponseDict]
    paypal: NotRequired[PayPalWalletResponse | PayPalWalletResponseDict]
    apple_pay: NotRequired[ApplePayPaymentObject | ApplePayPaymentObjectDict]
    google_pay: NotRequired[GooglePayWalletResponse | GooglePayWalletResponseDict]
    venmo: NotRequired[VenmoWalletResponse | VenmoWalletResponseDict]
