from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cobranded_card import CobrandedCard, CobrandedCardDict
from .pay_pal_wallet_vault_response import PayPalWalletVaultResponse, PayPalWalletVaultResponseDict


class PayPalWalletAttributesResponse(SdkBaseModel):
    """Additional attributes associated with the use of a PayPal Wallet."""

    vault: Optional[PayPalWalletVaultResponse] = UNSET
    """The details about a saved PayPal Wallet payment source."""

    cobranded_cards: Optional[list[CobrandedCard]] = UNSET
    """An array of merchant cobranded cards used by buyer to complete an order. This array will be present if a merchant
    has onboarded their cobranded card with PayPal and provided corresponding label(s)."""


class PayPalWalletAttributesResponseDict(TypedDict):
    vault: NotRequired[PayPalWalletVaultResponse | PayPalWalletVaultResponseDict]
    cobranded_cards: NotRequired[list[CobrandedCard | CobrandedCardDict]]
