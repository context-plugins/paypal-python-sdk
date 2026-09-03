from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VenmoPaymentTokenUsagePattern(str, Enum):
    """Expected business/pricing model for the billing agreement."""

    IMMEDIATE = "IMMEDIATE"
    """On-demand instant payments – non-recurring, pre-paid, variable amount, variable frequency."""

    DEFERRED = "DEFERRED"
    """Pay after use, non-recurring post-paid, variable amount, irregular frequency."""

    RECURRING_PREPAID = "RECURRING_PREPAID"
    """Pay upfront fixed or variable amount on a fixed date before the goods/service is delivered."""

    RECURRING_POSTPAID = "RECURRING_POSTPAID"
    """Pay on a fixed date based on usage or consumption after the goods/service is delivered."""

    THRESHOLD_PREPAID = "THRESHOLD_PREPAID"
    """Charge payer when the set amount is reached or monthly billing cycle, whichever comes first, before the
    goods/service is delivered."""

    THRESHOLD_POSTPAID = "THRESHOLD_POSTPAID"
    """Charge payer when the set amount is reached or monthly billing cycle, whichever comes first, after the
    goods/service is delivered."""

    __str__ = str.__str__


VenmoPaymentTokenUsagePatternOrStr: TypeAlias = Annotated[
    VenmoPaymentTokenUsagePattern | str, open_enum_validator(VenmoPaymentTokenUsagePattern)
]
