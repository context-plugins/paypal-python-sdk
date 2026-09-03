from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_information import CustomerInformation, CustomerInformationDict
from .vault_instruction import VaultInstruction, VaultInstructionDict


class ApplePayAttributes(SdkBaseModel):
    """Additional attributes associated with apple pay."""

    customer: Optional[CustomerInformation] = UNSET
    """This object represents a merchant’s customer, allowing them to store contact details, and track all payments
    associated with the same customer."""

    vault: Optional[VaultInstruction] = UNSET
    """Base vaulting specification. The object can be extended for specific use cases within each payment_source that
    supports vaulting."""


class ApplePayAttributesDict(TypedDict):
    customer: NotRequired[CustomerInformation | CustomerInformationDict]
    vault: NotRequired[VaultInstruction | VaultInstructionDict]
