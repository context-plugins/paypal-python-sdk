from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict
from .payment_token_response import PaymentTokenResponse, PaymentTokenResponseDict
from .vault_response_customer import VaultResponseCustomer, VaultResponseCustomerDict


class CustomerVaultPaymentTokensResponse(SdkBaseModel):
    """Collection of payment tokens saved for a given customer."""

    total_items: Optional[int] = UNSET
    """Total number of items."""

    total_pages: Optional[int] = UNSET
    """Total number of pages."""

    customer: Optional[VaultResponseCustomer] = UNSET
    """This object defines a customer in your system. Use it to manage customer profiles, save payment methods and
    contact details."""

    payment_tokens: Optional[list[PaymentTokenResponse]] = UNSET
    links: Optional[list[LinkDescription]] = UNSET
    """An array of related `HATEOAS links <https://developer.paypal.com/api/rest/responses/#hateoas>`__."""


class CustomerVaultPaymentTokensResponseDict(TypedDict):
    total_items: NotRequired[int]
    total_pages: NotRequired[int]
    customer: NotRequired[VaultResponseCustomer | VaultResponseCustomerDict]
    payment_tokens: NotRequired[list[PaymentTokenResponse | PaymentTokenResponseDict]]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
