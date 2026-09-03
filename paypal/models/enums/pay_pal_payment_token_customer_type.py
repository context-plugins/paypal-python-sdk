from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayPalPaymentTokenCustomerType(str, Enum):
    """The customer type associated with the PayPal payment token. This is to indicate whether the customer acting on
    the merchant / platform is either a business or a consumer., The customer type associated with a digital wallet
    payment token. This is to indicate whether the customer acting on the merchant / platform is either a business or a
    consumer."""

    CONSUMER = "CONSUMER"
    """The customer vaulting the PayPal payment token is a consumer on the merchant / platform."""

    BUSINESS = "BUSINESS"
    """The customer vaulting the PayPal payment token is a business on merchant / platform."""

    __str__ = str.__str__


PayPalPaymentTokenCustomerTypeOrStr: TypeAlias = Annotated[
    PayPalPaymentTokenCustomerType | str, open_enum_validator(PayPalPaymentTokenCustomerType)
]
