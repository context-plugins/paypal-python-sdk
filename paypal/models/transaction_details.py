from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auction_information import AuctionInformation, AuctionInformationDict
from .cart_information import CartInformation, CartInformationDict
from .incentive_information import IncentiveInformation, IncentiveInformationDict
from .payer_information import PayerInformation, PayerInformationDict
from .shipping_information import ShippingInformation, ShippingInformationDict
from .store_information import StoreInformation, StoreInformationDict
from .transaction_information import TransactionInformation, TransactionInformationDict


class TransactionDetails(SdkBaseModel):
    """The transaction details."""

    transaction_info: Optional[TransactionInformation] = UNSET
    """The transaction information."""

    payer_info: Optional[PayerInformation] = UNSET
    """The payer information."""

    shipping_info: Optional[ShippingInformation] = UNSET
    """The shipping information."""

    cart_info: Optional[CartInformation] = UNSET
    """The cart information."""

    store_info: Optional[StoreInformation] = UNSET
    """The store information."""

    auction_info: Optional[AuctionInformation] = UNSET
    """The auction information."""

    incentive_info: Optional[IncentiveInformation] = UNSET
    """The incentive details."""


class TransactionDetailsDict(TypedDict):
    transaction_info: NotRequired[TransactionInformation | TransactionInformationDict]
    payer_info: NotRequired[PayerInformation | PayerInformationDict]
    shipping_info: NotRequired[ShippingInformation | ShippingInformationDict]
    cart_info: NotRequired[CartInformation | CartInformationDict]
    store_info: NotRequired[StoreInformation | StoreInformationDict]
    auction_info: NotRequired[AuctionInformation | AuctionInformationDict]
    incentive_info: NotRequired[IncentiveInformation | IncentiveInformationDict]
