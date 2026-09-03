from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.card_brand import CardBrandOrStr


class NetworkTransaction(SdkBaseModel):
    """Reference values used by the card network to identify a transaction."""

    id: Optional[str] = UNSET
    """Transaction reference id returned by the scheme. For Visa and Amex, this is the "Tran id" field in response. For
    MasterCard, this is the "BankNet reference id" field in response. For Discover, this is the "NRID" field in
    response. The pattern we expect for this field from Visa/Amex/CB/Discover is numeric, Mastercard/BNPP is
    alphanumeric and Paysecure is alphanumeric with special character -."""

    date: Optional[str] = UNSET
    """The date that the transaction was authorized by the scheme. This field may not be returned for all networks.
    MasterCard refers to this field as "BankNet reference date". For some specific networks, such as MasterCard and
    Discover, this date field is mandatory when the ``previous_network_transaction_reference_id`` is passed."""

    network: Optional[CardBrandOrStr] = UNSET
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    acquirer_reference_number: Optional[str] = UNSET
    """Reference ID issued for the card transaction. This ID can be used to track the transaction across processors,
    card brands and issuing banks."""


class NetworkTransactionDict(TypedDict):
    id: NotRequired[str]
    date: NotRequired[str]
    network: NotRequired[CardBrandOrStr]
    acquirer_reference_number: NotRequired[str]
