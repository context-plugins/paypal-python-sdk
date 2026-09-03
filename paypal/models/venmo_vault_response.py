from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_information import CustomerInformation, CustomerInformationDict
from .enums.venmo_vault_response_status import VenmoVaultResponseStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict


class VenmoVaultResponse(SdkBaseModel):
    """The details about a saved venmo payment source."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the saved payment source."""

    status: Optional[VenmoVaultResponseStatusOrStr] = UNSET
    """The vault status."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related HATEOAS links."""

    customer: Optional[CustomerInformation] = UNSET
    """This object represents a merchant’s customer, allowing them to store contact details, and track all payments
    associated with the same customer."""


class VenmoVaultResponseDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[VenmoVaultResponseStatusOrStr]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    customer: NotRequired[CustomerInformation | CustomerInformationDict]
