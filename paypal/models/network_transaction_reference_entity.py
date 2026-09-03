from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.card_brand import CardBrandOrStr


class NetworkTransactionReferenceEntity(SdkBaseModel):
    """Previous network transaction reference including id and network."""

    id: str
    """Transaction reference id returned by the scheme. For Visa and Amex, this is the "Tran id" field in response. For
    MasterCard, this is the "BankNet reference id" field in response. For Discover, this is the "NRID" field in
    response. The pattern we expect for this field from Visa/Amex/CB/Discover is numeric, Mastercard/BNPP is
    alphanumeric and Paysecure is alphanumeric with special character -."""

    date: Optional[str] = UNSET
    """The date that the transaction was authorized by the scheme. This field may not be returned for all networks.
    MasterCard refers to this field as "BankNet reference date."""

    network: Optional[CardBrandOrStr] = UNSET
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""


class NetworkTransactionReferenceEntityDict(TypedDict):
    id: str
    date: NotRequired[str]
    network: NotRequired[CardBrandOrStr]
    time: NotRequired[str]
