from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.interval_unit import IntervalUnitOrStr


class Frequency(SdkBaseModel):
    """The frequency of the billing cycle."""

    interval_unit: IntervalUnitOrStr
    """The interval at which the subscription is charged or billed."""

    interval_count: Optional[int] = UNSET
    """The number of intervals after which a subscriber is billed. For example, if the ``interval_unit`` is ``DAY`` with
    an ``interval_count`` of ``2``, the subscription is billed once every two days. The following table lists the
    maximum allowed values for the ``interval_count`` for each ``interval_unit``: Interval unit Maximum interval count
    DAY 365 WEEK 52 MONTH 12 YEAR 1"""


class FrequencyDict(TypedDict):
    interval_unit: IntervalUnitOrStr
    interval_count: NotRequired[int]
