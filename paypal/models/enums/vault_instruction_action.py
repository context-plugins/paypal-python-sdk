from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VaultInstructionAction(str, Enum):
    """Vault Instruction on action to be performed after a successful payer approval."""

    ON_CREATE_PAYMENT_TOKENS = "ON_CREATE_PAYMENT_TOKENS"
    """Vault the payment method after API caller performs a successful POST on Payment Tokens."""

    ON_PAYER_APPROVAL = "ON_PAYER_APPROVAL"
    """Vault the payment method on successful payer authentication and approval."""

    __str__ = str.__str__


VaultInstructionActionOrStr: TypeAlias = Annotated[
    VaultInstructionAction | str, open_enum_validator(VaultInstructionAction)
]
