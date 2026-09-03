from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CancelSubscriptionRequest(SdkBaseModel):
    """The cancel subscription request details."""

    reason: str
    """The reason for the cancellation of a subscription."""


class CancelSubscriptionRequestDict(TypedDict):
    reason: str
