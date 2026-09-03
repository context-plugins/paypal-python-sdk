from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict
from .transaction_details import TransactionDetails, TransactionDetailsDict


class SearchResponse(SdkBaseModel):
    """The search response information."""

    transaction_details: Optional[list[TransactionDetails]] = UNSET
    """An array of transaction detail objects."""

    account_number: Optional[str] = UNSET
    """The merchant account number."""

    start_date: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    end_date: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    last_refreshed_datetime: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    page: Optional[int] = UNSET
    """A zero-relative index of transactions."""

    total_items: Optional[int] = UNSET
    """The total number of transactions as an integer beginning with the specified ``page`` in the full result and not
    just in this response."""

    total_pages: Optional[int] = UNSET
    """The total number of pages, as an ``integer``, when the ``total_items`` is divided into pages of the specified
    ``page_size``."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links
    <https://developer.paypal.com/api/rest/responses/#hateoas-links>`__."""


class SearchResponseDict(TypedDict):
    transaction_details: NotRequired[list[TransactionDetails | TransactionDetailsDict]]
    account_number: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    last_refreshed_datetime: NotRequired[str]
    page: NotRequired[int]
    total_items: NotRequired[int]
    total_pages: NotRequired[int]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
