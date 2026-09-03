from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .venmo_wallet_customer_information import VenmoWalletCustomerInformation, VenmoWalletCustomerInformationDict
from .venmo_wallet_vault_attributes import VenmoWalletVaultAttributes, VenmoWalletVaultAttributesDict


class VenmoWalletAdditionalAttributes(SdkBaseModel):
    """Additional attributes associated with the use of this Venmo Wallet."""

    customer: Optional[VenmoWalletCustomerInformation] = UNSET
    """The details about a customer in PayPal's system of record."""

    vault: Optional[VenmoWalletVaultAttributes] = UNSET
    """Resource consolidating common request and response attirbutes for vaulting Venmo Wallet."""


class VenmoWalletAdditionalAttributesDict(TypedDict):
    customer: NotRequired[VenmoWalletCustomerInformation | VenmoWalletCustomerInformationDict]
    vault: NotRequired[VenmoWalletVaultAttributes | VenmoWalletVaultAttributesDict]
