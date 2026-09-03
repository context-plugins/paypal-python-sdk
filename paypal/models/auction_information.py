from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuctionInformation(SdkBaseModel):
    """The auction information."""

    auction_site: Optional[str] = UNSET
    """The name of the auction site."""

    auction_item_site: Optional[str] = UNSET
    """The auction site URL."""

    auction_buyer_id: Optional[str] = UNSET
    """The ID of the buyer who makes the purchase in the auction. This ID might be different from the payer ID provided
    for the payment."""

    auction_closing_date: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""


class AuctionInformationDict(TypedDict):
    auction_site: NotRequired[str]
    auction_item_site: NotRequired[str]
    auction_buyer_id: NotRequired[str]
    auction_closing_date: NotRequired[str]
