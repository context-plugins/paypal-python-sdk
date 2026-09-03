from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentTokenStatus(str, Enum):
    """The status of the payment token."""

    CREATED = "CREATED"
    """A setup token is initialized with minimal information, more data must be added to the setup-token to be
    vaulted"""

    PAYER_ACTION_REQUIRED = "PAYER_ACTION_REQUIRED"
    """A contingency on payer approval is required before the payment method can be saved."""

    APPROVED = "APPROVED"
    """Setup token is ready to be vaulted. If a buyer approval contigency was returned, it is has been approved."""

    VAULTED = "VAULTED"
    """The payment token has been vaulted."""

    TOKENIZED = "TOKENIZED"
    """A vaulted payment method token has been tokenized for short term (one time) use."""

    __str__ = str.__str__


PaymentTokenStatusOrStr: TypeAlias = Annotated[PaymentTokenStatus | str, open_enum_validator(PaymentTokenStatus)]
