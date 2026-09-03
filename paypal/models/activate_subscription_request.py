from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ActivateSubscriptionRequest(SdkBaseModel):
    """The activate subscription request details."""

    reason: Optional[str] = UNSET
    """The reason for activation of a subscription. Required to reactivate the subscription."""


class ActivateSubscriptionRequestDict(TypedDict):
    reason: NotRequired[str]
