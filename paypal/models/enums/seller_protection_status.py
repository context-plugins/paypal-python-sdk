from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SellerProtectionStatus(str, Enum):
    """Indicates whether the transaction is eligible for seller protection. For information, see `PayPal Seller
    Protection for Merchants <https://www.paypal.com/us/webapps/mpp/security/seller-protection>`__."""

    ELIGIBLE = "ELIGIBLE"
    """Your PayPal balance remains intact if the customer claims that they did not receive an item or the account holder
    claims that they did not authorize the payment."""

    PARTIALLY_ELIGIBLE = "PARTIALLY_ELIGIBLE"
    """Your PayPal balance remains intact if the customer claims that they did not receive an item."""

    NOT_ELIGIBLE = "NOT_ELIGIBLE"
    """This transaction is not eligible for seller protection."""

    __str__ = str.__str__


SellerProtectionStatusOrStr: TypeAlias = Annotated[
    SellerProtectionStatus | str, open_enum_validator(SellerProtectionStatus)
]
