from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.tenure_type import TenureTypeOrStr
from .pricing_scheme import PricingScheme, PricingSchemeDict


class BillingCycle(SdkBaseModel):
    """The billing cycle providing details of the billing frequency, amount, duration and if the billing cycle is a
    free, discounted or regular billing cycle. The sequence of the billing cycle will be in the following order - free
    trial billing cycle(s), discounted trial billing cycle(s), regular billing cycle(s)."""

    tenure_type: TenureTypeOrStr
    """The tenure type of the billing cycle identifies if the billing cycle is a trial(free or discounted) or regular
    billing cycle."""

    pricing_scheme: Optional[PricingScheme] = UNSET
    """The pricing scheme details."""

    total_cycles: Optional[int] = UNSET
    """The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number
    of times (value between 1 and 999 for total_cycles). Regular billing cycles can be executed infinite times (value of
    0 for total_cycles) or a finite number of times (value between 1 and 999 for total_cycles)."""

    sequence: Optional[int] = UNSET
    """The order in which this cycle is to run among other billing cycles. For example, a trial billing cycle has a
    ``sequence`` of ``1`` while a regular billing cycle has a ``sequence`` of ``2``, so that trial cycle runs before the
    regular cycle."""

    start_date: Optional[str] = UNSET
    """The stand-alone date, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. To
    represent special legal values, such as a date of birth, you should use dates with no associated time or time-zone
    data. Whenever possible, use the standard ``date_time`` type. This regular expression does not validate all dates.
    For example, February 31 is valid and nothing is known about leap years."""


class BillingCycleDict(TypedDict):
    tenure_type: TenureTypeOrStr
    pricing_scheme: NotRequired[PricingScheme | PricingSchemeDict]
    total_cycles: NotRequired[int]
    sequence: NotRequired[int]
    start_date: NotRequired[str]
