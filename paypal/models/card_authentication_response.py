from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .three_d_secure_card_authentication_response import (
    ThreeDSecureCardAuthenticationResponse,
    ThreeDSecureCardAuthenticationResponseDict,
)


class CardAuthenticationResponse(SdkBaseModel):
    """Results of Authentication such as 3D Secure."""

    three_d_secure: Optional[ThreeDSecureCardAuthenticationResponse] = UNSET
    """Results of 3D Secure Authentication."""


class CardAuthenticationResponseDict(TypedDict):
    three_d_secure: NotRequired[ThreeDSecureCardAuthenticationResponse | ThreeDSecureCardAuthenticationResponseDict]
