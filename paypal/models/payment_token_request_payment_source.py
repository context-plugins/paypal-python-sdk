from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_token_request_card import PaymentTokenRequestCard, PaymentTokenRequestCardDict
from .vault_token_request import VaultTokenRequest, VaultTokenRequestDict


class PaymentTokenRequestPaymentSource(SdkBaseModel):
    """The payment method to vault with the instrument details."""

    card: Optional[PaymentTokenRequestCard] = UNSET
    """A Resource representing a request to vault a Card."""

    token: Optional[VaultTokenRequest] = UNSET
    """The Tokenized Payment Source representing a Request to Vault a Token."""


class PaymentTokenRequestPaymentSourceDict(TypedDict):
    card: NotRequired[PaymentTokenRequestCard | PaymentTokenRequestCardDict]
    token: NotRequired[VaultTokenRequest | VaultTokenRequestDict]
