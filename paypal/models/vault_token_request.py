from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.vault_token_request_type import VaultTokenRequestTypeOrStr


class VaultTokenRequest(SdkBaseModel):
    """The Tokenized Payment Source representing a Request to Vault a Token."""

    id: str
    """The PayPal-generated ID for the token."""

    type_: VaultTokenRequestTypeOrStr = Field(alias="type")
    """The tokenization method that generated the ID."""


class VaultTokenRequestDict(TypedDict):
    id: str
    type_: VaultTokenRequestTypeOrStr
