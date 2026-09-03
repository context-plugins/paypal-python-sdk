from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BlikOneClickPaymentRequest(SdkBaseModel):
    """Information used to pay using BLIK one-click flow."""

    auth_code: Optional[str] = UNSET
    """The 6-digit code used to authenticate a consumer within BLIK."""

    consumer_reference: str
    """The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and
    a merchant."""

    alias_label: Optional[str] = UNSET
    """A bank defined identifier used as a display name to allow the payer to differentiate between multiple registered
    bank accounts."""

    alias_key: Optional[str] = UNSET
    """A Blik-defined identifier for a specific Blik-enabled bank account that is associated with a given merchant. Used
    only in conjunction with a Consumer Reference."""


class BlikOneClickPaymentRequestDict(TypedDict):
    auth_code: NotRequired[str]
    consumer_reference: str
    alias_label: NotRequired[str]
    alias_key: NotRequired[str]
