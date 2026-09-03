from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.enrollment_status import EnrollmentStatusOrStr
from .enums.pares_status import ParesStatusOrStr


class ThreeDSecureCardAuthenticationResponse(SdkBaseModel):
    """Results of 3D Secure Authentication."""

    authentication_status: Optional[ParesStatusOrStr] = UNSET
    """Transactions status result identifier. The outcome of the issuer's authentication."""

    enrollment_status: Optional[EnrollmentStatusOrStr] = UNSET
    """Status of Authentication eligibility."""

    authentication_id: Optional[str] = UNSET
    """The externally received 3ds authentication id, to be returned in card detokenization response."""


class ThreeDSecureCardAuthenticationResponseDict(TypedDict):
    authentication_status: NotRequired[ParesStatusOrStr]
    enrollment_status: NotRequired[EnrollmentStatusOrStr]
    authentication_id: NotRequired[str]
