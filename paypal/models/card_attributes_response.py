from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_vault_response import CardVaultResponse, CardVaultResponseDict


class CardAttributesResponse(SdkBaseModel):
    """Additional attributes associated with the use of this card."""

    vault: Optional[CardVaultResponse] = UNSET
    """The details about a saved Card payment source."""


class CardAttributesResponseDict(TypedDict):
    vault: NotRequired[CardVaultResponse | CardVaultResponseDict]
