from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_pricing_scheme import SubscriptionPricingScheme, SubscriptionPricingSchemeDict


class UpdatePricingScheme(SdkBaseModel):
    """The update pricing scheme request details."""

    billing_cycle_sequence: int
    """The billing cycle sequence."""

    pricing_scheme: SubscriptionPricingScheme
    """The pricing scheme details."""


class UpdatePricingSchemeDict(TypedDict):
    billing_cycle_sequence: int
    pricing_scheme: SubscriptionPricingScheme | SubscriptionPricingSchemeDict
