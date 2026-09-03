from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GooglePayExperienceContext(SdkBaseModel):
    """Customizes the payer experience during the approval process for the payment."""

    return_url: str
    """Describes the URL."""

    cancel_url: str
    """Describes the URL."""


class GooglePayExperienceContextDict(TypedDict):
    return_url: str
    cancel_url: str
