from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CardExperienceContext(SdkBaseModel):
    """Customizes the payer experience during the 3DS Approval for payment."""

    return_url: Optional[str] = UNSET
    """Describes the URL."""

    cancel_url: Optional[str] = UNSET
    """Describes the URL."""


class CardExperienceContextDict(TypedDict):
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
