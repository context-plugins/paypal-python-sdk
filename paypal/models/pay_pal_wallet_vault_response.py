from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pay_pal_wallet_vault_status import PayPalWalletVaultStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .pay_pal_wallet_customer import PayPalWalletCustomer, PayPalWalletCustomerDict


class PayPalWalletVaultResponse(SdkBaseModel):
    """The details about a saved PayPal Wallet payment source."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the saved payment source."""

    status: Optional[PayPalWalletVaultStatusOrStr] = UNSET
    """The vault status."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related HATEOAS links."""

    customer: Optional[PayPalWalletCustomer] = UNSET
    """The details about a customer in PayPal's system of record."""


class PayPalWalletVaultResponseDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[PayPalWalletVaultStatusOrStr]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    customer: NotRequired[PayPalWalletCustomer | PayPalWalletCustomerDict]
