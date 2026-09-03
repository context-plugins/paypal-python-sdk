from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.authorization_incomplete_reason import AuthorizationIncompleteReasonOrStr


class AuthorizationStatusDetails(SdkBaseModel):
    """The details of the authorized payment status."""

    reason: Optional[AuthorizationIncompleteReasonOrStr] = UNSET
    """The reason why the authorized status is ``PENDING``."""


class AuthorizationStatusDetailsDict(TypedDict):
    reason: NotRequired[AuthorizationIncompleteReasonOrStr]
