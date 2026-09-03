from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OsType(str, Enum):
    """Operating System type of the device that the buyer is using."""

    ANDROID = "ANDROID"
    """Google Android OS."""

    IOS = "IOS"
    """Apple OS typically found in Apple mobile devices."""

    OTHER = "OTHER"
    """Any other OS type."""

    __str__ = str.__str__


OsTypeOrStr: TypeAlias = Annotated[OsType | str, open_enum_validator(OsType)]
