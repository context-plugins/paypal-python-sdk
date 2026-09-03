from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PricingModel(str, Enum):
    """The pricing model for the billing cycle."""

    FIXED = "FIXED"
    """A fixed pricing scheme where the customer is charged a fixed amount."""

    VARIABLE = "VARIABLE"
    """A variable pricing scheme where the customer is charged a variable amount."""

    AUTO_RELOAD = "AUTO_RELOAD"
    """A auto-reload pricing scheme where the customer is charged a fixed amount for reload."""

    __str__ = str.__str__


PricingModelOrStr: TypeAlias = Annotated[PricingModel | str, open_enum_validator(PricingModel)]
