from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SuspendSubscription(SdkBaseModel):
    """The suspend subscription request details."""

    reason: str
    """The reason for suspension of the Subscription."""


class SuspendSubscriptionDict(TypedDict):
    reason: str
