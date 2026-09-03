from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CaptureType(str, Enum):
    """The type of capture."""

    OUTSTANDING_BALANCE = "OUTSTANDING_BALANCE"
    """The outstanding balance that the subscriber must clear."""

    __str__ = str.__str__


CaptureTypeOrStr: TypeAlias = Annotated[CaptureType | str, open_enum_validator(CaptureType)]
