from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.vault_status import VaultStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .vault_customer import VaultCustomer, VaultCustomerDict


class VaultResponse(SdkBaseModel):
    """The details about a saved payment source."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the saved payment source."""

    status: Optional[VaultStatusOrStr] = UNSET
    """The vault status."""

    customer: Optional[VaultCustomer] = UNSET
    """This object represents a merchant’s customer, allowing them to store contact details, and track all payments
    associated with the same customer."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related HATEOAS links."""


class VaultResponseDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[VaultStatusOrStr]
    customer: NotRequired[VaultCustomer | VaultCustomerDict]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
