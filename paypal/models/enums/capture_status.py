from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CaptureStatus(str, Enum):
    """The status of the captured payment."""

    COMPLETED = "COMPLETED"
    """The funds for this captured payment were credited to the payee's PayPal account."""

    DECLINED = "DECLINED"
    """The funds could not be captured."""

    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"
    """An amount less than this captured payment's amount was partially refunded to the payer."""

    PENDING = "PENDING"
    """The funds for this captured payment was not yet credited to the payee's PayPal account. For more information, see
    status.details."""

    REFUNDED = "REFUNDED"
    """An amount greater than or equal to this captured payment's amount was refunded to the payer."""

    FAILED = "FAILED"
    """There was an error while capturing payment."""

    __str__ = str.__str__


CaptureStatusOrStr: TypeAlias = Annotated[CaptureStatus | str, open_enum_validator(CaptureStatus)]
