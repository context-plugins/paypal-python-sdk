from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_payment_object import ApplePayPaymentObject, ApplePayPaymentObjectDict
from .bancontact_payment_object import BancontactPaymentObject, BancontactPaymentObjectDict
from .blik_payment_object import BlikPaymentObject, BlikPaymentObjectDict
from .card_response import CardResponse, CardResponseDict
from .eps_payment_object import EpsPaymentObject, EpsPaymentObjectDict
from .giropay_payment_object import GiropayPaymentObject, GiropayPaymentObjectDict
from .google_pay_wallet_response import GooglePayWalletResponse, GooglePayWalletResponseDict
from .i_deal_payment_object import IDealPaymentObject, IDealPaymentObjectDict
from .my_bank_payment_object import MyBankPaymentObject, MyBankPaymentObjectDict
from .p24_payment_object import P24PaymentObject, P24PaymentObjectDict
from .pay_pal_wallet_response import PayPalWalletResponse, PayPalWalletResponseDict
from .sofort_payment_object import SofortPaymentObject, SofortPaymentObjectDict
from .trustly_payment_object import TrustlyPaymentObject, TrustlyPaymentObjectDict
from .venmo_wallet_response import VenmoWalletResponse, VenmoWalletResponseDict


class PaymentSourceResponse(SdkBaseModel):
    """The payment source used to fund the payment."""

    card: Optional[CardResponse] = UNSET
    """The payment card to use to fund a payment. Card can be a credit or debit card."""

    paypal: Optional[PayPalWalletResponse] = UNSET
    """The PayPal Wallet response."""

    bancontact: Optional[BancontactPaymentObject] = UNSET
    """Information used to pay Bancontact."""

    blik: Optional[BlikPaymentObject] = UNSET
    """Information used to pay using BLIK."""

    eps: Optional[EpsPaymentObject] = UNSET
    """Information used to pay using eps."""

    giropay: Optional[GiropayPaymentObject] = UNSET
    """Information needed to pay using giropay."""

    ideal: Optional[IDealPaymentObject] = UNSET
    """Information used to pay using iDEAL."""

    mybank: Optional[MyBankPaymentObject] = UNSET
    """Information used to pay using MyBank."""

    p24: Optional[P24PaymentObject] = UNSET
    """Information used to pay using P24(Przelewy24)."""

    sofort: Optional[SofortPaymentObject] = UNSET
    """Information used to pay using Sofort."""

    trustly: Optional[TrustlyPaymentObject] = UNSET
    """Information needed to pay using Trustly."""

    apple_pay: Optional[ApplePayPaymentObject] = UNSET
    """Information needed to pay using ApplePay."""

    google_pay: Optional[GooglePayWalletResponse] = UNSET
    """Google Pay Wallet payment data."""

    venmo: Optional[VenmoWalletResponse] = UNSET
    """Venmo wallet response."""


class PaymentSourceResponseDict(TypedDict):
    card: NotRequired[CardResponse | CardResponseDict]
    paypal: NotRequired[PayPalWalletResponse | PayPalWalletResponseDict]
    bancontact: NotRequired[BancontactPaymentObject | BancontactPaymentObjectDict]
    blik: NotRequired[BlikPaymentObject | BlikPaymentObjectDict]
    eps: NotRequired[EpsPaymentObject | EpsPaymentObjectDict]
    giropay: NotRequired[GiropayPaymentObject | GiropayPaymentObjectDict]
    ideal: NotRequired[IDealPaymentObject | IDealPaymentObjectDict]
    mybank: NotRequired[MyBankPaymentObject | MyBankPaymentObjectDict]
    p24: NotRequired[P24PaymentObject | P24PaymentObjectDict]
    sofort: NotRequired[SofortPaymentObject | SofortPaymentObjectDict]
    trustly: NotRequired[TrustlyPaymentObject | TrustlyPaymentObjectDict]
    apple_pay: NotRequired[ApplePayPaymentObject | ApplePayPaymentObjectDict]
    google_pay: NotRequired[GooglePayWalletResponse | GooglePayWalletResponseDict]
    venmo: NotRequired[VenmoWalletResponse | VenmoWalletResponseDict]
