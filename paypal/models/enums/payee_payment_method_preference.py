from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayeePaymentMethodPreference(str, Enum):
    """The merchant-preferred payment methods."""

    UNRESTRICTED = "UNRESTRICTED"
    """Accepts any type of payment from the customer."""

    IMMEDIATE_PAYMENT_REQUIRED = "IMMEDIATE_PAYMENT_REQUIRED"
    """Accepts only immediate payment from the customer. For example, credit card, PayPal balance, or instant ACH.
    Ensures that at the time of capture, the payment does not have the ``pending`` status."""

    __str__ = str.__str__


PayeePaymentMethodPreferenceOrStr: TypeAlias = Annotated[
    PayeePaymentMethodPreference | str, open_enum_validator(PayeePaymentMethodPreference)
]
