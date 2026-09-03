from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RefundStatus(str, Enum):
    """The status of the refund."""

    CANCELLED = "CANCELLED"
    """The refund was cancelled."""

    FAILED = "FAILED"
    """The refund could not be processed."""

    PENDING = "PENDING"
    """The refund is pending. For more information, see status_details.reason."""

    COMPLETED = "COMPLETED"
    """The funds for this transaction were debited to the customer's account."""

    __str__ = str.__str__


RefundStatusOrStr: TypeAlias = Annotated[RefundStatus | str, open_enum_validator(RefundStatus)]
