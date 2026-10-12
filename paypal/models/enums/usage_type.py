from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UsageType(str, Enum):
    """The usage type associated with the PayPal payment token."""

    MERCHANT = "MERCHANT"
    """The PayPal Payment Token will be used for future transaction directly with a merchant."""

    PLATFORM = "PLATFORM"
    """The PayPal Payment Token will be used for future transaction on a platform. A platform is typically a marketplace
    or a channel that a payer can purchase goods and services from multiple merchants."""

    __str__ = str.__str__


UsageTypeOrStr: TypeAlias = Annotated[UsageType | str, open_enum_validator(UsageType)]
