from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LiabilityShiftIndicator(str, Enum):
    """Liability shift indicator. The outcome of the issuer's authentication."""

    NO = "NO"
    """Liability is with the merchant."""

    POSSIBLE = "POSSIBLE"
    """Liability may shift to the card issuer."""

    UNKNOWN = "UNKNOWN"
    """The authentication system is not available."""

    __str__ = str.__str__


LiabilityShiftIndicatorOrStr: TypeAlias = Annotated[
    LiabilityShiftIndicator | str, open_enum_validator(LiabilityShiftIndicator)
]
