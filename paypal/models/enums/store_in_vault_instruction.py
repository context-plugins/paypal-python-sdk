from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StoreInVaultInstruction(str, Enum):
    """Defines how and when the payment source gets vaulted."""

    ON_SUCCESS = "ON_SUCCESS"
    """Defines that the payment_source will be vaulted only when at least one authorization or capture using that
    payment_source is successful."""

    __str__ = str.__str__


StoreInVaultInstructionOrStr: TypeAlias = Annotated[
    StoreInVaultInstruction | str, open_enum_validator(StoreInVaultInstruction)
]
