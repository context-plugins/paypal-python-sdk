from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pricing_model import PricingModelOrStr
from .money import Money, MoneyDict


class PricingScheme(SdkBaseModel):
    """The pricing scheme details."""

    price: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    pricing_model: PricingModelOrStr
    """The pricing model for the billing cycle."""

    reload_threshold_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class PricingSchemeDict(TypedDict):
    price: NotRequired[Money | MoneyDict]
    pricing_model: PricingModelOrStr
    reload_threshold_amount: NotRequired[Money | MoneyDict]
