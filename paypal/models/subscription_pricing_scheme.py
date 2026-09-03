from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.subscription_pricing_model import SubscriptionPricingModelOrStr
from .money import Money, MoneyDict
from .pricing_tier import PricingTier, PricingTierDict


class SubscriptionPricingScheme(SdkBaseModel):
    """The pricing scheme details."""

    version: Optional[int] = UNSET
    """The version of the pricing scheme."""

    fixed_price: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    pricing_model: Optional[SubscriptionPricingModelOrStr] = UNSET
    """The pricing model for tiered plan. The ``tiers`` parameter is required."""

    tiers: Optional[list[PricingTier]] = UNSET
    """An array of pricing tiers which are used for billing volume/tiered plans. pricing_model field has to be
    specified."""

    create_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    update_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""


class SubscriptionPricingSchemeDict(TypedDict):
    version: NotRequired[int]
    fixed_price: NotRequired[Money | MoneyDict]
    pricing_model: NotRequired[SubscriptionPricingModelOrStr]
    tiers: NotRequired[list[PricingTier | PricingTierDict]]
    create_time: NotRequired[str]
    update_time: NotRequired[str]
