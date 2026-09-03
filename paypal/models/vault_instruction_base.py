from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.store_in_vault_instruction import StoreInVaultInstructionOrStr


class VaultInstructionBase(SdkBaseModel):
    """Basic vault instruction specification that can be extended by specific payment sources that supports vaulting."""

    store_in_vault: Optional[StoreInVaultInstructionOrStr] = UNSET
    """Defines how and when the payment source gets vaulted."""


class VaultInstructionBaseDict(TypedDict):
    store_in_vault: NotRequired[StoreInVaultInstructionOrStr]
