from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PhoneType(str, Enum):
    """The phone type."""

    FAX = "FAX"
    """Fax number."""

    HOME = "HOME"
    """Home phone number."""

    MOBILE = "MOBILE"
    """Mobile phone number."""

    OTHER = "OTHER"
    """Other phone number."""

    PAGER = "PAGER"
    """Pager number."""

    __str__ = str.__str__


PhoneTypeOrStr: TypeAlias = Annotated[PhoneType | str, open_enum_validator(PhoneType)]
