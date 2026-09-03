from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capture_status_details import CaptureStatusDetails, CaptureStatusDetailsDict
from .enums.capture_status import CaptureStatusOrStr


class CaptureStatusWithDetails(SdkBaseModel):
    """The status and status details of a captured payment."""

    status: Optional[CaptureStatusOrStr] = UNSET
    """The status of the captured payment."""

    status_details: Optional[CaptureStatusDetails] = UNSET
    """The details of the captured payment status."""


class CaptureStatusWithDetailsDict(TypedDict):
    status: NotRequired[CaptureStatusOrStr]
    status_details: NotRequired[CaptureStatusDetails | CaptureStatusDetailsDict]
