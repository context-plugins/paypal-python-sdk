from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VenmoPaymentTokenCustomerType(str, Enum):
    """The customer type associated with the Venmo payment token. This is to indicate whether the customer acting on the
    merchant / platform is either a business or a consumer."""

    CONSUMER = "CONSUMER"
    """The customer vaulting the Venmo payment token is a consumer on the merchant / platform."""

    BUSINESS = "BUSINESS"
    """The customer vaulting the Venmo payment token is a business on merchant / platform."""

    __str__ = str.__str__


VenmoPaymentTokenCustomerTypeOrStr: TypeAlias = Annotated[
    VenmoPaymentTokenCustomerType | str, open_enum_validator(VenmoPaymentTokenCustomerType)
]
