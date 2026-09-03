from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardVerificationStatus(str, Enum):
    """Verification status of Card."""

    VERIFIED = "VERIFIED"
    """Card has been verified"""

    FAILED = "FAILED"
    """Card verification has failed"""

    __str__ = str.__str__


CardVerificationStatusOrStr: TypeAlias = Annotated[
    CardVerificationStatus | str, open_enum_validator(CardVerificationStatus)
]
