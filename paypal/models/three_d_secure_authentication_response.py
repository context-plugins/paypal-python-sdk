from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.enrollment_status import EnrollmentStatusOrStr
from .enums.pares_status import ParesStatusOrStr


class ThreeDSecureAuthenticationResponse(SdkBaseModel):
    """Results of 3D Secure Authentication."""

    authentication_status: Optional[ParesStatusOrStr] = UNSET
    """Transactions status result identifier. The outcome of the issuer's authentication."""

    enrollment_status: Optional[EnrollmentStatusOrStr] = UNSET
    """Status of Authentication eligibility."""


class ThreeDSecureAuthenticationResponseDict(TypedDict):
    authentication_status: NotRequired[ParesStatusOrStr]
    enrollment_status: NotRequired[EnrollmentStatusOrStr]
