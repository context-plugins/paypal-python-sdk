from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ParesStatus(str, Enum):
    """Transactions status result identifier. The outcome of the issuer's authentication."""

    Y = "Y"
    """Successful authentication."""

    N = "N"
    """Failed authentication / account not verified / transaction denied."""

    U = "U"
    """Unable to complete authentication."""

    A = "A"
    """Successful attempts transaction."""

    C = "C"
    """Challenge required for authentication."""

    R = "R"
    """Authentication rejected (merchant must not submit for authorization)."""

    D = "D"
    """Challenge required; decoupled authentication confirmed."""

    I_ = "I"
    """Informational only; 3DS requestor challenge preference acknowledged."""

    __str__ = str.__str__


ParesStatusOrStr: TypeAlias = Annotated[ParesStatus | str, open_enum_validator(ParesStatus)]
