from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .balance_information import BalanceInformation, BalanceInformationDict


class BalancesResponse(SdkBaseModel):
    """The balances response information."""

    balances: Optional[list[BalanceInformation]] = UNSET
    """An array of balance detail objects."""

    account_id: Optional[str] = UNSET
    """The PayPal payer ID, which is a masked version of the PayPal account number intended for use with third parties.
    The account number is reversibly encrypted and a proprietary variant of Base32 is used to encode the result."""

    as_of_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    last_refresh_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""


class BalancesResponseDict(TypedDict):
    balances: NotRequired[list[BalanceInformation | BalanceInformationDict]]
    account_id: NotRequired[str]
    as_of_time: NotRequired[str]
    last_refresh_time: NotRequired[str]
