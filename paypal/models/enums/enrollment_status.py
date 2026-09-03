from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EnrollmentStatus(str, Enum):
    """Status of Authentication eligibility."""

    Y = "Y"
    """Yes. The bank is participating in 3-D Secure protocol and will return the ACSUrl."""

    N = "N"
    """No. The bank is not participating in 3-D Secure protocol."""

    U = "U"
    """Unavailable. The DS or ACS is not available for authentication at the time of the request."""

    B = "B"
    """Bypass. The merchant authentication rule is triggered to bypass authentication."""

    __str__ = str.__str__


EnrollmentStatusOrStr: TypeAlias = Annotated[EnrollmentStatus | str, open_enum_validator(EnrollmentStatus)]
