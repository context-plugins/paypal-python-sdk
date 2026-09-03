from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_customer import CardCustomer, CardCustomerDict
from .card_verification import CardVerification, CardVerificationDict
from .vault_instruction_base import VaultInstructionBase, VaultInstructionBaseDict


class SubscriptionsCardAttributes(SdkBaseModel):
    """Additional attributes associated with the use of this card."""

    customer: Optional[CardCustomer] = UNSET
    """The details about a customer in PayPal's system of record."""

    vault: Optional[VaultInstructionBase] = UNSET
    """Basic vault instruction specification that can be extended by specific payment sources that supports vaulting."""

    verification: Optional[CardVerification] = UNSET
    """The API caller can opt in to verify the card through PayPal offered verification services (e.g. Smart Dollar
    Auth, 3DS)."""


class SubscriptionsCardAttributesDict(TypedDict):
    customer: NotRequired[CardCustomer | CardCustomerDict]
    vault: NotRequired[VaultInstructionBase | VaultInstructionBaseDict]
    verification: NotRequired[CardVerification | CardVerificationDict]
