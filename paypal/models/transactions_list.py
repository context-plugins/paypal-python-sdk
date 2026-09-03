from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict
from .subscription_transaction_details import SubscriptionTransactionDetails, SubscriptionTransactionDetailsDict


class TransactionsList(SdkBaseModel):
    """The list transactions for a subscription request details."""

    transactions: Optional[list[SubscriptionTransactionDetails]] = UNSET
    """An array of transactions."""

    total_items: Optional[int] = UNSET
    """The total number of items."""

    total_pages: Optional[int] = UNSET
    """The total number of pages."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""


class TransactionsListDict(TypedDict):
    transactions: NotRequired[list[SubscriptionTransactionDetails | SubscriptionTransactionDetailsDict]]
    total_items: NotRequired[int]
    total_pages: NotRequired[int]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
