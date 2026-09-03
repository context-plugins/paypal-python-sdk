from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisbursementMode(str, Enum):
    """The funds that are held on behalf of the merchant."""

    INSTANT = "INSTANT"
    """The funds are released to the merchant immediately."""

    DELAYED = "DELAYED"
    """The funds are held for a finite number of days. The actual duration depends on the region and type of
    integration. You can release the funds through a referenced payout. Otherwise, the funds disbursed automatically
    after the specified duration."""

    __str__ = str.__str__


DisbursementModeOrStr: TypeAlias = Annotated[DisbursementMode | str, open_enum_validator(DisbursementMode)]
