from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.store_in_vault_instruction import StoreInVaultInstructionOrStr


class VaultInstruction(SdkBaseModel):
    """Base vaulting specification. The object can be extended for specific use cases within each payment_source that
    supports vaulting."""

    store_in_vault: StoreInVaultInstructionOrStr
    """Defines how and when the payment source gets vaulted."""


class VaultInstructionDict(TypedDict):
    store_in_vault: StoreInVaultInstructionOrStr
