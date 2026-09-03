from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RefundIncompleteReason(str, Enum):
    """The reason why the refund has the ``PENDING`` or ``FAILED`` status."""

    ECHECK = "ECHECK"
    """The customer's account is funded through an eCheck, which has not yet cleared."""

    __str__ = str.__str__


RefundIncompleteReasonOrStr: TypeAlias = Annotated[
    RefundIncompleteReason | str, open_enum_validator(RefundIncompleteReason)
]
