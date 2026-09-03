from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict
from .transaction_search_error_details import TransactionSearchErrorDetails, TransactionSearchErrorDetailsDict


class DefaultError(SdkBaseModel):
    """The error details."""

    name: str
    """The human-readable, unique name of the error."""

    message: str
    """The message that describes the error."""

    debug_id: str
    """The PayPal internal ID. Used for correlation purposes."""

    information_link: Optional[str] = UNSET
    """The information link, or URI, that shows detailed information about this error for the developer."""

    details: Optional[list[TransactionSearchErrorDetails]] = UNSET
    """An array of additional details about the error."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""


class DefaultErrorDict(TypedDict):
    name: str
    message: str
    debug_id: str
    information_link: NotRequired[str]
    details: NotRequired[list[TransactionSearchErrorDetails | TransactionSearchErrorDetailsDict]]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
