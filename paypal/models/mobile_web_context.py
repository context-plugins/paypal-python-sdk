from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mobile_return_flow import MobileReturnFlowOrStr


class MobileWebContext(SdkBaseModel):
    """Buyer's mobile web browser context to app switch to the PayPal consumer app."""

    return_flow: Optional[MobileReturnFlowOrStr] = UNSET
    """Merchant preference on how the buyer can navigate back to merchant website post approving the transaction on the
    PayPal App."""

    buyer_user_agent: Optional[str] = UNSET
    """User agent from the request originating from the buyer's device. This will be used to identify the buyer's
    operating system and browser versions. NOTE: Merchants must not alter or modify the buyer's device user agent."""


class MobileWebContextDict(TypedDict):
    return_flow: NotRequired[MobileReturnFlowOrStr]
    buyer_user_agent: NotRequired[str]
