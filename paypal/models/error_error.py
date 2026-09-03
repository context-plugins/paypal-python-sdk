from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_details import ErrorDetails, ErrorDetailsDict
from .link_description import LinkDescription, LinkDescriptionDict


class ErrorError(SdkBaseModel):
    """The error details."""

    name: str
    """The human-readable, unique name of the error."""

    message: str
    """The message that describes the error."""

    debug_id: str
    """The PayPal internal ID. Used for correlation purposes."""

    details: Optional[list[ErrorDetails]] = UNSET
    """An array of additional details about the error."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links
    <https://developer.paypal.com/api/rest/responses/#hateoas-links>`__."""


class ErrorErrorDict(TypedDict):
    name: str
    message: str
    debug_id: str
    details: NotRequired[list[ErrorDetails | ErrorDetailsDict]]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
