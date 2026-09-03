from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .venmo_vault_response import VenmoVaultResponse, VenmoVaultResponseDict


class VenmoWalletAttributesResponse(SdkBaseModel):
    """Additional attributes associated with the use of a Venmo Wallet."""

    vault: Optional[VenmoVaultResponse] = UNSET
    """The details about a saved venmo payment source."""


class VenmoWalletAttributesResponseDict(TypedDict):
    vault: NotRequired[VenmoVaultResponse | VenmoVaultResponseDict]
