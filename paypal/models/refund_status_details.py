from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.refund_incomplete_reason import RefundIncompleteReasonOrStr


class RefundStatusDetails(SdkBaseModel):
    """The details of the refund status."""

    reason: Optional[RefundIncompleteReasonOrStr] = UNSET
    """The reason why the refund has the ``PENDING`` or ``FAILED`` status."""


class RefundStatusDetailsDict(TypedDict):
    reason: NotRequired[RefundIncompleteReasonOrStr]
