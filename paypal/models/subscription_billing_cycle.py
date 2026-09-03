from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.tenure_type import TenureTypeOrStr
from .frequency import Frequency, FrequencyDict
from .subscription_pricing_scheme import SubscriptionPricingScheme, SubscriptionPricingSchemeDict


class SubscriptionBillingCycle(SdkBaseModel):
    """The billing cycle details."""

    pricing_scheme: Optional[SubscriptionPricingScheme] = UNSET
    """The pricing scheme details."""

    frequency: Frequency
    """The frequency of the billing cycle."""

    tenure_type: TenureTypeOrStr
    """The tenure type of the billing cycle. In case of a plan having trial cycle, only 2 trial cycles are allowed per
    plan."""

    sequence: int
    """The order in which this cycle is to run among other billing cycles. For example, a trial billing cycle has a
    ``sequence`` of ``1`` while a regular billing cycle has a ``sequence`` of ``2``, so that trial cycle runs before the
    regular cycle."""

    total_cycles: Optional[int] = UNSET
    """The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number
    of times (value between 1 and 999 for total_cycles). Regular billing cycles can be executed infinite times (value of
    0 for total_cycles) or a finite number of times (value between 1 and 999 for total_cycles)."""


class SubscriptionBillingCycleDict(TypedDict):
    pricing_scheme: NotRequired[SubscriptionPricingScheme | SubscriptionPricingSchemeDict]
    frequency: Frequency | FrequencyDict
    tenure_type: TenureTypeOrStr
    sequence: int
    total_cycles: NotRequired[int]
