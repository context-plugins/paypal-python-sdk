from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReasonCode(str, Enum):
    """The reason code for the payment failure."""

    PAYMENT_DENIED = "PAYMENT_DENIED"
    """PayPal declined the payment due to one or more customer issues."""

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    """An internal server error has occurred."""

    PAYEE_ACCOUNT_RESTRICTED = "PAYEE_ACCOUNT_RESTRICTED"
    """The payee account is not in good standing and cannot receive payments."""

    PAYER_ACCOUNT_RESTRICTED = "PAYER_ACCOUNT_RESTRICTED"
    """The payer account is not in good standing and cannot make payments."""

    PAYER_CANNOT_PAY = "PAYER_CANNOT_PAY"
    """Payer cannot pay for this transaction."""

    SENDING_LIMIT_EXCEEDED = "SENDING_LIMIT_EXCEEDED"
    """The transaction exceeds the payer's sending limit."""

    TRANSACTION_RECEIVING_LIMIT_EXCEEDED = "TRANSACTION_RECEIVING_LIMIT_EXCEEDED"
    """The transaction exceeds the receiver's receiving limit."""

    CURRENCY_MISMATCH = "CURRENCY_MISMATCH"
    """The transaction is declined due to a currency mismatch."""

    __str__ = str.__str__


ReasonCodeOrStr: TypeAlias = Annotated[ReasonCode | str, open_enum_validator(ReasonCode)]
