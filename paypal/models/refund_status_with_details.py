from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.refund_status import RefundStatusOrStr
from .refund_status_details import RefundStatusDetails, RefundStatusDetailsDict


class RefundStatusWithDetails(SdkBaseModel):
    """The refund status with details."""

    status: Optional[RefundStatusOrStr] = UNSET
    """The status of the refund."""

    status_details: Optional[RefundStatusDetails] = UNSET
    """The details of the refund status."""


class RefundStatusWithDetailsDict(TypedDict):
    status: NotRequired[RefundStatusOrStr]
    status_details: NotRequired[RefundStatusDetails | RefundStatusDetailsDict]
