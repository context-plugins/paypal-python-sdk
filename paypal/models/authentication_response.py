from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.liability_shift_indicator import LiabilityShiftIndicatorOrStr
from .three_d_secure_authentication_response import (
    ThreeDSecureAuthenticationResponse,
    ThreeDSecureAuthenticationResponseDict,
)


class AuthenticationResponse(SdkBaseModel):
    """Results of Authentication such as 3D Secure."""

    liability_shift: Optional[LiabilityShiftIndicatorOrStr] = UNSET
    """Liability shift indicator. The outcome of the issuer's authentication."""

    three_d_secure: Optional[ThreeDSecureAuthenticationResponse] = UNSET
    """Results of 3D Secure Authentication."""


class AuthenticationResponseDict(TypedDict):
    liability_shift: NotRequired[LiabilityShiftIndicatorOrStr]
    three_d_secure: NotRequired[ThreeDSecureAuthenticationResponse | ThreeDSecureAuthenticationResponseDict]
