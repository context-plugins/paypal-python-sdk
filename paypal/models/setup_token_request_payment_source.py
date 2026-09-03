from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_request import BankRequest, BankRequestDict
from .setup_token_request_card import SetupTokenRequestCard, SetupTokenRequestCardDict
from .vault_apple_pay_request import VaultApplePayRequest, VaultApplePayRequestDict
from .vault_pay_pal_wallet_request import VaultPayPalWalletRequest, VaultPayPalWalletRequestDict
from .vault_token_request import VaultTokenRequest, VaultTokenRequestDict
from .vault_venmo_request import VaultVenmoRequest, VaultVenmoRequestDict


class SetupTokenRequestPaymentSource(SdkBaseModel):
    """The payment method to vault with the instrument details."""

    card: Optional[SetupTokenRequestCard] = UNSET
    """A Resource representing a request to vault a Card."""

    paypal: Optional[VaultPayPalWalletRequest] = UNSET
    """A resource representing a request to vault PayPal Wallet."""

    venmo: Optional[VaultVenmoRequest] = UNSET
    """A resource representing a request to vault Venmo."""

    apple_pay: Optional[VaultApplePayRequest] = UNSET
    """A resource representing a request to vault Apple Pay."""

    token: Optional[VaultTokenRequest] = UNSET
    """The Tokenized Payment Source representing a Request to Vault a Token."""

    bank: Optional[BankRequest] = UNSET
    """A Resource representing a request to vault a Bank used for ACH Debit."""


class SetupTokenRequestPaymentSourceDict(TypedDict):
    card: NotRequired[SetupTokenRequestCard | SetupTokenRequestCardDict]
    paypal: NotRequired[VaultPayPalWalletRequest | VaultPayPalWalletRequestDict]
    venmo: NotRequired[VaultVenmoRequest | VaultVenmoRequestDict]
    apple_pay: NotRequired[VaultApplePayRequest | VaultApplePayRequestDict]
    token: NotRequired[VaultTokenRequest | VaultTokenRequestDict]
    bank: NotRequired[BankRequest | BankRequestDict]
