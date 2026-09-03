from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MerchantPreferences(SdkBaseModel):
    """The merchant preferences for a subscription."""

    return_url: Optional[str] = UNSET
    """The URL where the customer is redirected after the customer approves the payment."""

    cancel_url: Optional[str] = UNSET
    """The URL where the customer is redirected after the customer cancels the payment."""


class MerchantPreferencesDict(TypedDict):
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
