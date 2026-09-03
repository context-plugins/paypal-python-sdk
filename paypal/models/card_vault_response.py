from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_customer_information import CardCustomerInformation, CardCustomerInformationDict
from .enums.vault_status import VaultStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict


class CardVaultResponse(SdkBaseModel):
    """The details about a saved Card payment source."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the saved payment source."""

    status: Optional[VaultStatusOrStr] = UNSET
    """The vault status."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related HATEOAS links."""

    customer: Optional[CardCustomerInformation] = UNSET
    """The details about a customer in PayPal's system of record."""


class CardVaultResponseDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[VaultStatusOrStr]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    customer: NotRequired[CardCustomerInformation | CardCustomerInformationDict]
