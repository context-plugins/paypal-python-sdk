from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_request import ApplePayRequest, ApplePayRequestDict
from .bancontact_payment_request import BancontactPaymentRequest, BancontactPaymentRequestDict
from .blik_payment_request import BlikPaymentRequest, BlikPaymentRequestDict
from .card_request import CardRequest, CardRequestDict
from .eps_payment_request import EpsPaymentRequest, EpsPaymentRequestDict
from .giropay_payment_request import GiropayPaymentRequest, GiropayPaymentRequestDict
from .google_pay_request import GooglePayRequest, GooglePayRequestDict
from .i_deal_payment_request import IDealPaymentRequest, IDealPaymentRequestDict
from .my_bank_payment_request import MyBankPaymentRequest, MyBankPaymentRequestDict
from .p24_payment_request import P24PaymentRequest, P24PaymentRequestDict
from .pay_pal_wallet import PayPalWallet, PayPalWalletDict
from .sofort_payment_request import SofortPaymentRequest, SofortPaymentRequestDict
from .token import Token, TokenDict
from .trustly_payment_request import TrustlyPaymentRequest, TrustlyPaymentRequestDict
from .venmo_wallet_request import VenmoWalletRequest, VenmoWalletRequestDict


class PaymentSource(SdkBaseModel):
    """The payment source definition."""

    card: Optional[CardRequest] = UNSET
    """The payment card to use to fund a payment. Can be a credit or debit card. Note: Passing card number, cvv and
    expiry directly via the API requires PCI SAQ D compliance. *PayPal offers a mechanism by which you do not have to
    take on the PCI SAQ D burden by using hosted fields - refer to this Integration Guide*."""

    token: Optional[Token] = UNSET
    """The tokenized payment source to fund a payment."""

    paypal: Optional[PayPalWallet] = UNSET
    """A resource that identifies a PayPal Wallet is used for payment."""

    bancontact: Optional[BancontactPaymentRequest] = UNSET
    """Information needed to pay using Bancontact."""

    blik: Optional[BlikPaymentRequest] = UNSET
    """Information needed to pay using BLIK."""

    eps: Optional[EpsPaymentRequest] = UNSET
    """Information needed to pay using eps."""

    giropay: Optional[GiropayPaymentRequest] = UNSET
    """Information needed to pay using giropay."""

    ideal: Optional[IDealPaymentRequest] = UNSET
    """Information needed to pay using iDEAL."""

    mybank: Optional[MyBankPaymentRequest] = UNSET
    """Information needed to pay using MyBank."""

    p24: Optional[P24PaymentRequest] = UNSET
    """Information needed to pay using P24 (Przelewy24)."""

    sofort: Optional[SofortPaymentRequest] = UNSET
    """Information needed to pay using Sofort."""

    trustly: Optional[TrustlyPaymentRequest] = UNSET
    """Information needed to pay using Trustly."""

    apple_pay: Optional[ApplePayRequest] = UNSET
    """Information needed to pay using ApplePay."""

    google_pay: Optional[GooglePayRequest] = UNSET
    """Information needed to pay using Google Pay."""

    venmo: Optional[VenmoWalletRequest] = UNSET
    """Information needed to pay using Venmo."""


class PaymentSourceDict(TypedDict):
    card: NotRequired[CardRequest | CardRequestDict]
    token: NotRequired[Token | TokenDict]
    paypal: NotRequired[PayPalWallet | PayPalWalletDict]
    bancontact: NotRequired[BancontactPaymentRequest | BancontactPaymentRequestDict]
    blik: NotRequired[BlikPaymentRequest | BlikPaymentRequestDict]
    eps: NotRequired[EpsPaymentRequest | EpsPaymentRequestDict]
    giropay: NotRequired[GiropayPaymentRequest | GiropayPaymentRequestDict]
    ideal: NotRequired[IDealPaymentRequest | IDealPaymentRequestDict]
    mybank: NotRequired[MyBankPaymentRequest | MyBankPaymentRequestDict]
    p24: NotRequired[P24PaymentRequest | P24PaymentRequestDict]
    sofort: NotRequired[SofortPaymentRequest | SofortPaymentRequestDict]
    trustly: NotRequired[TrustlyPaymentRequest | TrustlyPaymentRequestDict]
    apple_pay: NotRequired[ApplePayRequest | ApplePayRequestDict]
    google_pay: NotRequired[GooglePayRequest | GooglePayRequestDict]
    venmo: NotRequired[VenmoWalletRequest | VenmoWalletRequestDict]
