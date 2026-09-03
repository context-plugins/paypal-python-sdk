from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .authorization_status_details import AuthorizationStatusDetails, AuthorizationStatusDetailsDict
from .enums.authorization_status import AuthorizationStatusOrStr


class AuthorizationStatusWithDetails(SdkBaseModel):
    """The status fields and status details for an authorized payment."""

    status: Optional[AuthorizationStatusOrStr] = UNSET
    """The status for the authorized payment."""

    status_details: Optional[AuthorizationStatusDetails] = UNSET
    """The details of the authorized payment status."""


class AuthorizationStatusWithDetailsDict(TypedDict):
    status: NotRequired[AuthorizationStatusOrStr]
    status_details: NotRequired[AuthorizationStatusDetails | AuthorizationStatusDetailsDict]
