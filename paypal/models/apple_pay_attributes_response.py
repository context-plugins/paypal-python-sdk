from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .vault_response import VaultResponse, VaultResponseDict


class ApplePayAttributesResponse(SdkBaseModel):
    """Additional attributes associated with the use of Apple Pay."""

    vault: Optional[VaultResponse] = UNSET
    """The details about a saved payment source."""


class ApplePayAttributesResponseDict(TypedDict):
    vault: NotRequired[VaultResponse | VaultResponseDict]
