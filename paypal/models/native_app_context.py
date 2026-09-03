from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.os_type import OsTypeOrStr


class NativeAppContext(SdkBaseModel):
    """Merchant provided, buyer's native app preferences to app switch to the PayPal consumer app."""

    os_type: Optional[OsTypeOrStr] = UNSET
    """Operating System type of the device that the buyer is using."""

    os_version: Optional[str] = UNSET
    """Operating System version of the device that the buyer is using."""


class NativeAppContextDict(TypedDict):
    os_type: NotRequired[OsTypeOrStr]
    os_version: NotRequired[str]
