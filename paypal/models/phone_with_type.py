from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.phone_type import PhoneTypeOrStr
from .phone_number import PhoneNumber, PhoneNumberDict


class PhoneWithType(SdkBaseModel):
    """The phone information."""

    phone_type: Optional[PhoneTypeOrStr] = UNSET
    """The phone type."""

    phone_number: PhoneNumber
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""


class PhoneWithTypeDict(TypedDict):
    phone_type: NotRequired[PhoneTypeOrStr]
    phone_number: PhoneNumber | PhoneNumberDict
