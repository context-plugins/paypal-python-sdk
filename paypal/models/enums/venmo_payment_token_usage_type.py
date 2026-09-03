from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VenmoPaymentTokenUsageType(str, Enum):
    """The usage type associated with the Venmo payment token."""

    MERCHANT = "MERCHANT"
    """The Venmo Payment Token will be used for future transaction directly with a merchant."""

    PLATFORM = "PLATFORM"
    """The Venmo Payment Token will be used for future transaction on a platform. A platform is typically a marketplace
    or a channel that a payer can purchase goods and services from multiple merchants."""

    __str__ = str.__str__


VenmoPaymentTokenUsageTypeOrStr: TypeAlias = Annotated[
    VenmoPaymentTokenUsageType | str, open_enum_validator(VenmoPaymentTokenUsageType)
]
