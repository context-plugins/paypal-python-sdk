from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.tenure_type import TenureTypeOrStr


class CycleExecution(SdkBaseModel):
    """The regular and trial execution details for a billing cycle."""

    tenure_type: TenureTypeOrStr
    """The type of the billing cycle."""

    sequence: int
    """The order in which to run this cycle among other billing cycles."""

    cycles_completed: int
    """The number of billing cycles that have completed."""

    cycles_remaining: Optional[int] = UNSET
    """For a finite billing cycle, cycles_remaining is the number of remaining cycles. For an infinite billing cycle,
    cycles_remaining is set as 0."""

    current_pricing_scheme_version: Optional[int] = UNSET
    """The active pricing scheme version for the billing cycle."""

    total_cycles: Optional[int] = UNSET
    """The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number
    of times (value between 1 and 999 for total_cycles). Regular billing cycles can be executed infinite times (value of
    0 for total_cycles) or a finite number of times (value between 1 and 999 for total_cycles)."""


class CycleExecutionDict(TypedDict):
    tenure_type: TenureTypeOrStr
    sequence: int
    cycles_completed: int
    cycles_remaining: NotRequired[int]
    current_pricing_scheme_version: NotRequired[int]
    total_cycles: NotRequired[int]
