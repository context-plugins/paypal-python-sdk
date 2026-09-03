from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_description import LinkDescription, LinkDescriptionDict


class ErrorDetails(SdkBaseModel):
    """The error details. Required for client-side ``4XX`` errors."""

    field: Optional[str] = UNSET
    """The field that caused the error. If this field is in the body, set this value to the field's JSON pointer value.
    Required for client-side errors."""

    value: Optional[str] = UNSET
    """The value of the field that caused the error."""

    location: Optional[str] = UNSET
    """The location of the field that caused the error. Value is ``body``, ``path``, or ``query``."""

    issue: str
    """The unique, fine-grained application-level error code."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related `HATEOAS links <https://developer.paypal.com/api/rest/responses/#hateoas-links>`__
    that are either relevant to the issue by providing additional information or offering potential resolutions."""

    description: Optional[str] = UNSET
    """The human-readable description for an issue. The description can change over the lifetime of an API, so clients
    must not depend on this value."""


class ErrorDetailsDict(TypedDict):
    field: NotRequired[str]
    value: NotRequired[str]
    location: NotRequired[str]
    issue: str
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    description: NotRequired[str]
