from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionPricingModel(str, Enum):
    """The pricing model for tiered plan. The ``tiers`` parameter is required."""

    VOLUME = "VOLUME"
    """A volume pricing model."""

    TIERED = "TIERED"
    """A tiered pricing model."""

    __str__ = str.__str__


SubscriptionPricingModelOrStr: TypeAlias = Annotated[
    SubscriptionPricingModel | str, open_enum_validator(SubscriptionPricingModel)
]
