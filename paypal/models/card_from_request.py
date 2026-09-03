from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardFromRequest(SdkBaseModel):
    """Representation of card details as received in the request."""

    expiry: Optional[str] = UNSET
    """The year and month, in ISO-8601 ``YYYY-MM`` date format. See `Internet date and time format
    <https://tools.ietf.org/html/rfc3339#section-5.6>`__."""

    last_digits: Optional[str] = UNSET
    """The last digits of the payment card."""


class CardFromRequestDict(TypedDict):
    expiry: NotRequired[str]
    last_digits: NotRequired[str]
