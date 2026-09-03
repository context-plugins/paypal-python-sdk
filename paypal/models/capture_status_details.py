from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.capture_incomplete_reason import CaptureIncompleteReasonOrStr


class CaptureStatusDetails(SdkBaseModel):
    """The details of the captured payment status."""

    reason: Optional[CaptureIncompleteReasonOrStr] = UNSET
    """The reason why the captured payment status is ``PENDING`` or ``DENIED``."""


class CaptureStatusDetailsDict(TypedDict):
    reason: NotRequired[CaptureIncompleteReasonOrStr]
