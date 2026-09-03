from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BlikOneClickPaymentObject(SdkBaseModel):
    """Information used to pay using BLIK one-click flow."""

    consumer_reference: Optional[str] = UNSET
    """The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and
    a merchant."""


class BlikOneClickPaymentObjectDict(TypedDict):
    consumer_reference: NotRequired[str]
