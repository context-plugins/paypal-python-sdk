from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInitiator(str, Enum):
    """The person or party who initiated or triggered the payment."""

    CUSTOMER = "CUSTOMER"
    """Payment is initiated with the active engagement of the customer. e.g. a customer checking out on a merchant
    website."""

    MERCHANT = "MERCHANT"
    """Payment is initiated by merchant on behalf of the customer without the active engagement of customer. e.g. a
    merchant charging the monthly payment of a subscription to the customer."""

    __str__ = str.__str__


PaymentInitiatorOrStr: TypeAlias = Annotated[PaymentInitiator | str, open_enum_validator(PaymentInitiator)]
